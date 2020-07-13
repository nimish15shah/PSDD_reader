
class OPERATOR():
  PRODUCT= 1
  SUM= 2
  LEAF= 3
  DIV= 4
    
#******    
#** Models a node in the AC 
#*****
class node():
  def __init__(self, node_key):
    self.key= node_key
    self.child_key_list= []
    self.parent_key_list= []
    self.operation_type= OPERATOR.PRODUCT
    self.depth_of_first_common_child= None
    
    #------Properties of BN-----------
    #---------------------------------
    #-- Leaf properteis (Only valid if operation_type=OPERATOR.LEAF)
    self.LEAF_TYPE_INVALID= 0 # Not a leaf
    self.LEAF_TYPE_INDICATOR= 1
    self.LEAF_TYPE_WEIGHT= 2
    self.leaf_type= self.LEAF_TYPE_INVALID
    #self.leaf_numeric_val=0.0 # Set to 1 for True/Don't care indicator and 0 for False indicator. Set to weight value if leaf type is LEAF_TYPE_WEIGHT
    self.leaf_literal_val= 0 # Literal value is the value that is in the line of this leaf node in .net.ac file
    
    #---- AC eval and error details------
    #------------------------------------
    # Important value during evaluation
    self.curr_val=0.0
    self.min_val=0.0
    self.max_val=1.0
    
    # Error modelling parameters
    self.rel_error_val= 2
    self.abs_error_val= 2
    self.bits= 32
    self.arith_type= 'fixed'

    # Level and reverse level
    # level: computed top-down.
    # reverse_level: computed bottom up.
    # In reverse_level, all the leaf node will be at zero level
    # In level, the leaf nodes entering high up in the heirarchy will have a higher level.
    self.level= None
    self.reverse_level= None

    # dfs level computed by a DFS traversal. Needed during decomposition
    self.dfs_level= None

  def get_self_key(self):
    return self.key

  def add_child(self, child_key): # child_key is a key for the child to be added
    assert isinstance(child_key, int), "child_key should be of int type"    
    self.child_key_list.append(child_key)
  
  def get_child_list(self):
    return self.child_key_list
  
  def add_parent(self, parent_key):
    assert isinstance(parent_key, int), "parent_key should be of int type"    
    self.parent_key_list.append(parent_key)
  
  def get_parent_list(self):
    return self.parent_key_list

  def set_operation(self, operation):
    self.operation_type= operation
   
  def print_attr(self):
    print("Self key: ", self.get_self_key(), end=' ')
    print("Children list: ", self.get_child_list(), end=' ')
    print("Parent list: ", self.get_parent_list(), end=' ')
    if (self.operation_type == OPERATOR.PRODUCT):
      print("Operation: Product")
    elif (self.operation_type == OPERATOR.SUM):
      print("Operation: Sum")
    elif (self.operation_type == OPERATOR.LEAF):
      print("Operation: Leaf")
    else:
      print(' ')
  
  # Methods to check type of node
  def is_head(self):
    if len(self.parent_key_list) == 0:  return True
    else: return False

  def is_leaf(self):
    if self.operation_type == OPERATOR.LEAF:
      return True
    else:
      return False

  def is_sum(self):
    if self.operation_type == OPERATOR.SUM:
      return True
    else:
      return False

  def is_prod(self):
    if self.operation_type == OPERATOR.PRODUCT:
      return True
    else:
      return False
  
  def is_weight(self):
    if self.is_leaf():
      assert self.leaf_type != self.LEAF_TYPE_INVALID
      if self.leaf_type == self.LEAF_TYPE_WEIGHT:
        return True
    return False

  def is_indicator(self):
    if self.is_leaf():
      assert self.leaf_type != self.LEAF_TYPE_INVALID
      if self.leaf_type == self.LEAF_TYPE_INDICATOR:
        return True
    return False

  # Methods to set type of node
  def set_sum(self):
    self.operation_type= OPERATOR.SUM

  def set_prod(self):
    self.operation_type= OPERATOR.PRODUCT
  
  def set_leaf_weight(self):
    self.operation_type= OPERATOR.LEAF
    self.leaf_type= self.LEAF_TYPE_WEIGHT
    self.computed = True

  def set_leaf_indicator(self):
    self.operation_type= OPERATOR.LEAF
    self.leaf_type= self.LEAF_TYPE_INDICATOR

