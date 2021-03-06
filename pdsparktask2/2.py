from __future__ import print_function

from pyspark import SparkContext, SparkConf

def parse_edge(s):
  user, follower = s.split('\t')
  return (int(user), int(follower))

def step(item):
  prev_v, next_v = item[0], item[1][1]
  return (next_v, prev_v)


config = SparkConf().setAppName('hw2').setMaster('yarn').set("spark.ui.port", "18089")
sc = SparkContext(conf=config)

n = 400 # number of partitions
edges = sc.textFile('/data/twitter/twitter_sample.txt').map(parse_edge)
forward_edges = edges.map(lambda e: (e[1], e[0])).partitionBy(n).cache()

start = 12
end = 34
parent_nodes = sc.parallelize([(start, -1)]).partitionBy(n)
candidates = sc.parallelize([(start, 0)])
while True:
    candidates = candidates.join(forward_edges, n).map(step)
    candidates = candidates.subtractByKey(parent_nodes, n)
    candidates = candidates.reduceByKey(lambda a, b: min(a, b))
    parent_nodes = parent_nodes.union(candidates).cache()
    candidates = candidates.map(lambda x: (x[0], 0)).cache()
    if len(candidates.lookup(end)) > 0:
        break

parent_nodes = parent_nodes.sortByKey().cache()

route = [end]
current_node = end
while current_node != start:
    current_node = parent_nodes.lookup(current_node)[0]
    route.append(current_node)

for node in reversed(route):
    if node == end:
        print(end)
        break
    print(node, end=",")
