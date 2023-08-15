from collections import deque
import time

def item_tree(item_id):
  """
  Return a tree rooted at item_id and its descendants
  Parameters
  ----------
  item_id : int
            A valid item id
  Returns
  -------
  graph_  : dict of lists
            Represents adjacency list, key of dict is item id
            values is list of item id that are immediate descendants
  """
  graph_ = dict()
  queue_ = deque() 
  uri_prefix = 'https://hacker-news.firebaseio.com/v0/'
  queue_.append(item_id)
  while queue_:
    id = queue_.popleft()
    response = requests.get(uri_prefix + f'item/{id}.json')
    if response.status_code == 200:
      data = response.json()
      kids = data.get('kids', [])
      graph_[id] = kids
      for kid in kids:
        queue_.append(kid)
  return graph_
