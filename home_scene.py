from camera_game_engine import GameScene
import cv2

class HomeScene(GameScene):
	def setup(self):
		self.elements["KEY_FUNCTION"] = {"type":"text", "message":"Home: Press 'p' to play", "x":30, "y":690, "font":cv2.FONT_HERSHEY_TRIPLEX, "size":1, "color":(255, 255, 255), "thickness":2}
			
	def reset(self):
		self.stage.setCapture(False) 

	def keyInToggle(self, key):
		if key & 0xFF == ord('p'):
			self.stage.jumpScene("PLAYING")
		elif key & 0xFF == ord('q'):			
			self.stage.quit()