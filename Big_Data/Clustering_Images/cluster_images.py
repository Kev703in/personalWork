# Clustering Images with K-Means
# Kevin Richard

## Imports:
import os
import numpy as np
import tensorflow as tf
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


## Constants:
# Image directory:
image_dir = './images'
image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir)]
# Similarity threshold:
similarity_threshold = 0.7
# Base model for extract features from images:
base_model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False)
model = tf.keras.Model(inputs=base_model.input, outputs=base_model.layers[-1].output)


class ClusterImages():
    def __init__(self, similarity_threshold, model):
        self.similarity_threshold = similarity_threshold
        self.model = model

    def extract_features(self, image_paths):
        features = []
        for path in image_paths:
            # Only resizeing image
            img = tf.keras.preprocessing.image.load_img(path, target_size=(224,224))
            # Convert to tf array, can also go with np, but tf easier?
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            # we use mobilenet preprocessing because the model used is mobilenet
            img_array = tf.keras.applications.mobilenet.preprocess_input(img_array)
            # adding position at the start to make it array, as most models expect array of inputs. (224,224) -> (1,224,224)
            img_array = np.expand_dims(img_array, axis=0)
            feature_vector = self.model.predict(img_array)
            features.append(feature_vector.flatten())
        image_features = np.array(features)
        return image_features
    
    # Cosine function to make similarity matrix
    def similarity_cosine_function(self,image_features):
        features_dot_product = np.dot(image_features,image_features.T)
        norms = np.linalg.norm(image_features, axis=1)   
        similarity_matrix = features_dot_product/np.outer(norms,norms)
        return similarity_matrix

    def similarity_cluster(self,image_paths,image_features,similarity_matrix):
        num_samples = image_features.shape[0]   # number of images
        num_clusters = 1    # initializze with one cluster
        cluster_labels = np.zeros(num_samples, dtype = int) # initialize cluster labels as 0

        while True:
            # sklearn cluster KMeans initialize.
            kmeans = KMeans(n_clusters=num_clusters, random_state=42)
            # Group all images to number of clusters (n_clusters) initialized
            labels = kmeans.fit_predict(image_features)
            avg_similarity_within_clusters = []
            # compare similarity of grouped clusters
            for label in range(num_clusters):
                # group clusters based on cluster_id each iteration
                cluster_indices = np.where( labels == label)[0]
                if len(cluster_indices > 1):
                    # avg of similarity indices within cluster. if cluster indices [7,8] : avg of (7,7), (7,8), (8,8), (8,7)
                    similarity_within_clusters = np.mean(similarity_matrix[np.ix_(cluster_indices,cluster_indices)])
                    avg_similarity_within_clusters.append(similarity_within_clusters)
            
            # Even if no clusters, will break if each image in individual cluster
            if all( similarity >= similarity_threshold for similarity in avg_similarity_within_clusters):
                cluster_labels = labels
                break
            num_clusters +=1

        print("optimal number of clusters = ",num_clusters)

        # Cluster in dictionary:
        clusters = {}
        for i, label in enumerate(cluster_labels):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(image_paths[i])
        return clusters

    # Main Function
    def cluster(self,image_paths):
        image_features = self.extract_features(image_paths)
        similarity_matrix = self.similarity_cosine_function(image_features)
        clusters = self.similarity_cluster(image_paths, image_features,similarity_matrix)
        return clusters
    
    # display view 1
    def displayClusters1(self,clusters):
        for cluster_id, cluster_images in clusters.items():
            print(f"Cluster : {cluster_id}")
            print(f"cluster_images : {cluster_images}")
            for image in cluster_images:
                img = tf.keras.preprocessing.image.load_img(image,target_size=(224,224))
                plt.figure(figsize=(2,2))
                plt.imshow(img)
                plt.axis('off')
                plt.show()

    # display view 2
    def displayClusters2(self,clusters):
        for cluster_id, cluster_images in clusters.items():
            print(f"Cluster: {cluster_id}")
            num_images = len(cluster_images)
            fig, axs = plt.subplots(1, num_images, figsize=(num_images * 2, 2))
            if num_images == 1:  
                axs = [axs]
            for i, image in enumerate(cluster_images):
                img = tf.keras.preprocessing.image.load_img(image, target_size=(224, 224))
                axs[i].imshow(img)
                axs[i].axis('off')
            plt.show()

if __name__ == '__main__':
    clusterApp = ClusterImages( similarity_threshold, model)
    clusters = clusterApp.cluster(image_paths)
    # clusterApp.displayClusters1(clusters)
    clusterApp.displayClusters2(clusters)