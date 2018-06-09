package interfaces;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

public class SokobanStandardSave implements SokobanSave {
	private SokobanBoard board;
	
	public SokobanStandardSave(SokobanBoard board) {
		this.board = board;
	}

	@Override
	public void save(String fileName) {
		String textBoard = board.getTextBoard();
		if (fileName.endsWith(".txt")) {
			try {
				PrintWriter outFile = new PrintWriter(fileName);
				outFile.println(textBoard);
				outFile.close();
				System.out.println("Game has been saved");
			} catch (FileNotFoundException e) {
				System.err.println("Error: file " + fileName + " could not be opened for writing");
				System.exit(1);
			}
		} else {
			System.out.println("Filename must end with .txt");
		}
	}

	@Override
	public String load(String fileName) {
		Scanner in;
		String textBoard = "";
		try {
			in = new Scanner(new FileReader(fileName));
			while(in.hasNext()) {
				textBoard += in.nextLine();
				if (in.hasNext()) {
					textBoard += "\n";
				}
			}
			in.close();
		} catch (FileNotFoundException e) {
			System.err.println("Error; file " + fileName + " could not be opened");
			System.exit(1);
		}
		return textBoard;
	}
}
