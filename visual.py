import psychopy.visual as visual
from psychopy.constants import FINISHED, NOT_STARTED, PAUSED, PLAYING, STOPPED

class MovieVisualizer(object):
  def __init__(self, win, filename, centerPosition, width):
    self.__filename = str(filename)
    
    self.component = visual.MovieStim(win, filename=filename)
    height = float(width) * self.component.format.height / self.component.format.width
    self.component.size = (width, height)
    self.component.pos = centerPosition
    
  def draw(self):
    self.component.draw()

  def restart(self, filename=None):
    if ((filename is None) or (filename == self.__filename)) and (self.component.status not in [FINISHED, STOPPED]):
      self.component.seek(0)
    else:
      if filename is not None:
        self.__filename = filename
      self.component.loadMovie(self.__filename)
    self.component.play()

  @property
  def stillRunning(self):
    return self.component.status == PLAYING
    
