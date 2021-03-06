class Cluster(object):
    """
    Cluster is set of nodes.
    """
    def __init__(self):
        self.nodes = []
        self.feature_vector = []  # each cluster has own feature vector generated by nodes' feature vector(f1+f2/n1+n2 term)

    def get_nodes(self):
        """
        Return a list of nodes of this cluster
        :return: A list of nodes of this cluster
        """
        return self.nodes[:]

    def get_feature_vector(self):
        """
        Return a feature vector of this cluster
        :return: A list of feature vector of this cluster
        """
        return self.feature_vector[:]

    def add_node(self, _input):
        """
        Add given node to this cluster
        :param _input: Node wanted to add in this cluster
        :return: None
        """
        self.nodes.append(_input)

    def remove_node(self, _input):
        """
        Remove given node to this cluster
        :param _input: Node wanted to remove in this cluster
        :return: None
        """
        self.nodes.remove(_input)

    def set_feature_vector(self, _input):
        """
        Add given feature vector to this cluster
        :param _input: feature vector (number)
        :return: None
        """
        self.feature_vector = _input[:]

    def __copy__(self):
        """
        Copy this cluster object
        :return: New copied cluster object
        """
        new = Cluster()
        new.nodes = self.nodes[:]
        new.feature_vector = self.feature_vector[:]
        return new
