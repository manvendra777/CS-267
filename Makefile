PYTHON := python3
COSINE_SIMILIARITY := cosine_similarity.py
KNN := knn.py
K_MEANS := k_means.py

# cosine similarity 
run-cosine:
	$(PYTHON) $(COSINE_SIMILIARITY)

# knn
run-knn: 
	$(PYTHON) $(KNN)

# k-means
run-kmeans:
	$(PYTHON) $(K_MEANS)