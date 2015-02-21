import math

class WordItemPresentation:
  def __init__(self, time=0, decay=0):
    self.decay = decay
    self.time = time

class WordItem:
  def __init__(self, name):
    self.name = name
    self.alpha = .25
    self.presentations = []

def _calculateDecayFromActivation(x, alpha):
  """
    Referred to as "d" in the equations
  """
  c = 0.2
  return c * math.exp(x) + alpha

def calculateActivation(wordItem, time, leaveout=0):
  if len(wordItem.presentations) - leaveout <= 0:
    raise ValueError("activaton undefined for item that was not presented yet")
  else:
    return math.log(sum([(time - presentation.time)**(-presentation.decay) for presentation in wordItem.presentations[:len(wordItem.presentations) - leaveout]])); #calculate activation of second to last

def calculateNewDecay(wordItem, time, leaveout=0):
  if len(wordItem.presentations) - leaveout <= 0:
    raise ValueError("item's presentation history is not long enough")
  elif len(wordItem.presentations) - leaveout == 1:
    return _calculateDecayFromActivation(0, wordItem.alpha)
  else:
    m = calculateActivation(wordItem, time, leaveout=leaveout)
    return _calculateDecayFromActivation(m, wordItem.alpha)
