package interfaces;

import java.util.Stack;

public class SokobanLog {
	private SokobanBoard board;
	private Stack<String> undo = new Stack<>();
	private Stack<String> redo = new Stack<>();
	
	public SokobanLog(SokobanBoard board) {
		this.board = board;
		undo.add(board.getTextBoard());
	}
	
	public void addUndo() {
		if (!getLastUndoBoard().equals(board.getTextBoard())) {
			undo.add(board.getTextBoard());
		}
	}
	
	public void addRedo() {
		if (!getLastRedoBoard().equals(board.getTextBoard())) {
			redo.add(board.getTextBoard());
		}
	}
	
	public void removeUndo() {
		undo.remove(undo.size() - 1);
	}
	
	public void removeRedo() {
		redo.remove(redo.size() - 1);
	}
	
	public String getLastUndoBoard() {
		if (undo.empty()) {
			return " ";
		}
		return undo.lastElement();
	}
	
	public String getLastRedoBoard() {
		if (redo.isEmpty()) {
			return " ";
		}
		return redo.lastElement();
	}
	
	public void removeAll() {
		undo.removeAllElements();
		redo.removeAllElements();
	}
	
	public void removeAllRedo() {
		redo.removeAllElements();
	}
	
	public boolean undoIsEmpty() {
		return undo.size() <= 1;
	}
	
	public boolean redoIsEmpty() {
		return redo.isEmpty();
	}
}
