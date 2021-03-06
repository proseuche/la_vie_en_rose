import DotParser
import HC
import SA
import MDG
import PSO
import TurboMQ
from WCA import WCA
import csv


# read .gv file(dot) and create graphs
def make_target_MDG(file_path):
    """
    Make MDG based on given file
    :param file_path: A path of dot file
    :return: MDG graph of given dot file
    """
    dot_file = DotParser.read_and_render('test/' + file_path)
    # print(dot_file.source)
    
    # get edge information and parse it
    edges = DotParser.parser(dot_file, "->")  # second argument should be "--" or "->" (depends on .dot file format)
    
    # make dependency graph and set feature vector
    targetMDG = MDG.MDG(edges)
    # print(targetMDG.edges)
    targetMDG.set_feature_vector()
    return targetMDG


def get_information(file_path):  # using target_MDG and a benchmark, create result
    """
    Execute Each algorithm for given file and return TurboMQ, cohesion, and coupling
    :param file_path: A path of dot file
    :return: Clustering result - value of TurboMQ, A list of [Cohesion, Coupling], A list of result clusters
    """
    targetMDG = make_target_MDG(file_path)
    methods = ['WCA', 'HC', 'WCA_HC', 'SA', 'WCA_SA', 'PSO', 'WCA_PSO']
    clusters_set = []
    TMQ = []
    cohe_coup = []
    print("====WCA start====\n")
    clusters_set.append(WCA(targetMDG))
    print("====WCA end====\n\n")
    
    print("====HC start====\n")
    clusters_set.append(HC.HC(targetMDG))
    print("====HC end====\n\n")
    
    print("====WCA_HC start====\n")
    clusters_set.append(HC.WCA_HC(targetMDG, WCA(targetMDG)))
    print("====WCA_HC end====\n\n")
    
    print("====SA start====\n")
    clusters_set.append(SA.SA(targetMDG))
    print("====SA end====\n\n")
    
    print("====WCA_SA start====\n")
    clusters_set.append(SA.WCA_SA(targetMDG, WCA(targetMDG)))
    print("====WCA_SA end====\n\n")
    
    print("====PSO start====\n\n")
    clusters_set.append(PSO.PSO(targetMDG))
    print("====PSO end====\n\n")
    
    print("====WCA_PSO start====\n\n")
    clusters_set.append(PSO.WCA_PSO(targetMDG, WCA(targetMDG)))
    print("====WCA_PSO end====\n\n")
    
    # get TMQ data
    for clusters in clusters_set:
        TMQ.append(TurboMQ.calculate_fitness(clusters, targetMDG))
        cohe_coup.append(TurboMQ.get_cohesion_coupling(clusters, targetMDG))
    # write result files
    for i in range(len(methods)):
        DotParser.write_file(file_path, methods[i], clusters_set[i], targetMDG)
        
    return TMQ, cohe_coup, clusters_set


def print_result(file_path):
    """
    Check each clustering algorithm for given file and print result and make csv file with result
    :return: None.
    """
    methods = ['WCA', 'HC', 'WCA_HC', 'SA', 'WCA_SA', 'PSO', 'WCA_PSO']
    
    # test for all benchmarks
    print("\n========file : " + file_path + "start ========\n")
    TMQ, cohe_coup, clusters_set = get_information(file_path)
    print("\n========file : " + file_path + "end ========\n\n\n")

    f = open('test/result/' + file_path[0:-4] + '.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow(['Algorithm', 'TurboMQ', 'Cohesion', 'Coupling'])
        
    # print Information
    print("\n=====Result=====")
    for j in range(len(methods)):
        print(file_path + " " + methods[j])
        print("TMQ= " + str(TMQ[j]) + ", " + "Cohesion= " + str(cohe_coup[j][0]) + ", " + "Coupling= " + str(cohe_coup[j][1])+"\n")
        wr.writerow([methods[j], TMQ[j], cohe_coup[j][0], cohe_coup[j][1]])

    f.close()
