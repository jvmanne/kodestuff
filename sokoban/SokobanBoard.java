package interfaces;

import java.util.Scanner;

public class SokobanBoard {
	private SokobanTile[][] board;
	private int level;
	private boolean levelOver;
	private SokobanLog log;
	private String startBoard;
	
	public SokobanBoard() {
		level = 1;
		levelOver = false;
		setGame(gameLevel());
		log = new SokobanLog(this);
	}
	
	public static void main(String[] args) {
		SokobanBoard board1 = new SokobanBoard();
		System.out.println("press 'a', 's', 'd' and 'w' to move or 'r' to restart");
		System.out.println(board1);
		while (!board1.isGameOver()) {
			Scanner scan = new Scanner(System.in);
			String s = scan.next();
			char direction = s.charAt(0);
			board1.move(direction);
			System.out.println(board1);
		}
	}
	
	private String gameLevel() {
		if (level == 0) {
			return startBoard;
		}
		if (level == 1) {
			return "#####\n"
				  +"#@$.#\n"
				  +"#####";
		} else if (level == 2) {
			return "###  \n#.###\n#*$ #\n# @ #\n#####";
		} else if (level == 3) {
			return "#######\n#.@ # #\n#$* $ #\n#   $ #\n# ..  #\n#  *  #\n#######";
		}
		return "*###########*\n#           #\n#  ... ...  #\n#  *$$ $.$  #\n# $*+$ $*$$ #\n#  *$$ $.$  #\n#  ...  .   #\n#           #\n*###########*";
	}
	
	public void setGame(String gameText) {
		String game = gameText;
		int x = 1;
		int y = 0;
		for (int i = 0; i < game.length(); i++) {
			y++;
			if (game.charAt(i) == '\n') {
				x++;
				y = 0;
			}
		}
		board = new SokobanTile[x][y];
		int i = 0;
		for (int row = 0; row < board.length; row++) {
			for (int col = 0; col < board[0].length; col++) {
				if (game.charAt(i) == '\n') {
					i++;
				}
				board[row][col] = new SokobanTile(game.charAt(i));
				i++;
			}
		}
	}
	
	public void restart() {
		if (level == 4 && isGameOver()) {
			level = 1;
		}
		setGame(gameLevel());
		log.removeAll();
		log.addUndo();
	}
	
	public void nextLevel() {
		level++;
		log.removeAll();
		setGame(gameLevel());
		log.addUndo();
	}
	
	public boolean isGameOver() {
		levelOver = false;
		for (int row = 0; row < board.length; row++) {
			for (int col = 0; col < board[0].length; col++) {
				if (board[row][col].getTile() == '$') {
					return false;
				}
			}
		}
		if (level < 4) {
			nextLevel();
			levelOver = true;
			return false;
		}
		return true;
	}
	
	public void move(char direction) throws IllegalArgumentException {
		if (direction != 'a' && direction != 's' && direction != 'd' && direction != 'w' && direction != 'r' && direction != 'u' && direction != 'i' && direction != 'j' && direction != 'k') {
			throw new IllegalArgumentException("Move with 'a', 's', 'd' and 'w'");
		}
		if (direction == 'r') {
			restart();
		} else if (isGameOver()) {
			
		} else {
			for (int row = 0; row < board.length; row++) {
				boolean done = false;
				for (int col = 0; col < board[0].length; col++) {
					if (board[row][col].isPlayer()) {
						if (direction == 'a') {
							moveLeft(row, col);
							log.removeAllRedo();
						} else if (direction == 's') {
							moveDown(row, col);
							log.removeAllRedo();
						} else if (direction == 'd') {
							moveRight(row, col);
							log.removeAllRedo();
						} else if (direction == 'w') {
							moveUp(row, col);
							log.removeAllRedo();
						} else if (direction == 'r') {
							restart();
						} else if (direction == 'u') {
							undo();
						} else if (direction == 'i') {
							redo();
						} else if (direction == 'j') {
							System.out.println("Filename: ");
							Scanner scan = new Scanner(System.in);
							String fileName = scan.next();
							save(fileName);
						} else if (direction == 'k') {
							System.out.println("Filename: ");
							Scanner scan = new Scanner(System.in);
							String fileName = scan.next();
							load(fileName);
						}
						done = true;
						log.addUndo();
						break;
					}
				}
				if (done) {
					break;
				}
			}
		}
	}
	public void moveLeft(int row, int col) {
		if (board[row][col-1].getTile() == ' ') {
			board[row][col-1].setTile('@');
		} else if (board[row][col-1].getTile() == '.') {
			board[row][col-1].setTile('+');
		} else if (board[row][col-1].isMovingTile() && board[row][col-2].isFreeTile()) {
			if (board[row][col-2].getTile() == ' ') {
				board[row][col-2].setTile('$');
			} else {
				board[row][col-2].setTile('*');
			}
			if (board[row][col-1].getTile() == '$') {
				board[row][col-1].setTile('@');
			} else {
				board[row][col-1].setTile('+');
			}
		}
		if (board[row][col-1].isPlayer()) {
			if (board[row][col].getTile() == '@') {
				board[row][col].setTile(' ');
			} else {
				board[row][col].setTile('.');
			}
		}
	}
	
	public void moveRight(int row, int col) {
		if (board[row][col+1].getTile() == ' ') {
			board[row][col+1].setTile('@');
		} else if (board[row][col+1].getTile() == '.') {
			board[row][col+1].setTile('+');
		} else if (board[row][col+1].isMovingTile() && board[row][col+2].isFreeTile()) {
			if (board[row][col+2].getTile() == ' ') {
				board[row][col+2].setTile('$');
			} else {
				board[row][col+2].setTile('*');
			}
			if (board[row][col+1].getTile() == '$') {
				board[row][col+1].setTile('@');
			} else {
				board[row][col+1].setTile('+');
			}
		}
		if (board[row][col+1].isPlayer()) {
			if (board[row][col].getTile() == '@') {
				board[row][col].setTile(' ');
			} else {
				board[row][col].setTile('.');
			}
		}
	}
	
	public void moveUp(int row, int col) {
		if (board[row-1][col].getTile() == ' ') {
			board[row-1][col].setTile('@');
		} else if (board[row-1][col].getTile() == '.') {
			board[row-1][col].setTile('+');
		} else if (board[row-1][col].isMovingTile() && board[row-2][col].isFreeTile()) {
			if (board[row-2][col].getTile() == ' ') {
				board[row-2][col].setTile('$');
			} else {
				board[row-2][col].setTile('*');
			}
			if (board[row-1][col].getTile() == '$') {
				board[row-1][col].setTile('@');
			} else {
				board[row-1][col].setTile('+');
			}
		}
		if (board[row-1][col].isPlayer()) {
			if (board[row][col].getTile() == '@') {
				board[row][col].setTile(' ');
			} else {
				board[row][col].setTile('.');
			}
		}
	}
	
	public void moveDown(int row, int col) {
		if (board[row+1][col].getTile() == ' ') {
			board[row+1][col].setTile('@');
		} else if (board[row+1][col].getTile() == '.') {
			board[row+1][col].setTile('+');
		} else if (board[row+1][col].isMovingTile() && board[row+2][col].isFreeTile()) {
			if (board[row+2][col].getTile() == ' ') {
				board[row+2][col].setTile('$');
			} else {
				board[row+2][col].setTile('*');
			}
			if (board[row+1][col].getTile() == '$') {
				board[row+1][col].setTile('@');
			} else {
				board[row+1][col].setTile('+');
			}
		}
		if (board[row+1][col].isPlayer()) {
			if (board[row][col].getTile() == '@') {
				board[row][col].setTile(' ');
			} else {
				board[row][col].setTile('.');
			}
	
		}
	}
	
	private String write() {
		StringBuffer aString = new StringBuffer();
		aString.append("Level " + level + "\n");
		for (int row = 0; row < board.length; row++) {
			for (int col = 0; col < board[0].length; col++) {
				aString.append(board[row][col] + " ");
			}
			aString.append("\n");
		}
		return aString.toString();
	}
	
	public String getTextBoard() {
		String textBoard = "";
		for (int row = 0; row < board.length; row++) {
			for (int col = 0; col < board[0].length; col++) {
				textBoard += board[row][col] + "";
			}
			textBoard += "\n";
		}
		return textBoard;
	}
	
	public void change(String game) {
		int x = 1;
		int y = 0;
		for (int i = 0; i < game.length(); i++) {
			y++;
			if (game.charAt(i) == '\n') {
				x++;
				y = 0;
			}
		}
		int i = 0;
		for (int row = 0; row < board.length; row++) {
			for (int col = 0; col < board[0].length; col++) {
				if (game.charAt(i) == '\n') {
					i++;
				}
				board[row][col] = new SokobanTile(game.charAt(i));
				i++;
			}
		}
	}
	
	public void undo() {
		if (!log.undoIsEmpty()) {
			log.addRedo();
			log.removeUndo();
			change(log.getLastUndoBoard());

		}
	}
	
	public void redo() {
		if (!log.redoIsEmpty()) {
			change(log.getLastRedoBoard());
			log.addUndo();
			log.removeRedo();
		}
	}
	
	public void save(String fileName) {
		SokobanSave save = new SokobanStandardSave(this);
		save.save(fileName);
	}
	
	public void load(String fileName) {
		SokobanSave save = new SokobanStandardSave(this);
		String textBoard = save.load(fileName);
		startBoard = textBoard;
		level = 0;
		setGame(gameLevel());
		toString();
		log.removeAll();
	}
	
	public String toString() {
		String textBoard = write();
		if (isGameOver()) {
			return textBoard + "\n" + "Congratulations you've won the game" + "\n" + "Press 'r' to restart";
		}
		if (levelOver) {
			return write() + "\n" + "\n" + textBoard;
		}
		return textBoard;
	}
}
