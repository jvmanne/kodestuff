package interfaces;

public class SokobanTile {
	char tile;
	
	public SokobanTile(char tile) throws IllegalArgumentException{
		if (tile != ' ' && tile != '#' && tile != '.' && tile != '$' && tile != '*' && tile != '@' && tile != '+') {
			throw new IllegalArgumentException("Tile does not exist");
		}
		this.tile = tile;
	}
	
	public char getTile() {
		return tile;
	}
	
	public void setTile(char tile) {
		if (tile != ' ' && tile != '#' && tile != '.' && tile != '$' && tile != '*' && tile != '@' && tile != '+') {
			throw new IllegalArgumentException("Tile does not exist");
		}
		this.tile = tile;
	}
	
	public boolean isMovingTile() {
		return tile == '@' || tile == '+' || tile == '$' || tile == '*';
	}
	
	public boolean isFreeTile() {
		return tile == ' ' || tile == '.';
	}
	
	public boolean isPlayer() {
		return tile == '@' || tile == '+';
	}
	
	public String toString() {
		return String.valueOf(getTile());
	}
}
