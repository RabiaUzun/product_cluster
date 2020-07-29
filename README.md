# Product Cluster
Product Cluster computes the minimum edit distance between strings with dynamic programming and clusters most similar
string together. It also ignores language-specific characters in Turkish language to be able to have a better score.

**Installation**

Clone the repository and create a virtual environment.

$ git clone https://github.com/RabiaUzun/product_cluster.git
$ cd product_cluster
$ virtualenv -p python3 env
$ source env/bin/activate

**Run**

$ python prepare_data_file.py