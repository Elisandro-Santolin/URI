package albumsoap;

import java.util.ArrayList;

public class Acervo {
	private ArrayList<Album> acervo = new ArrayList<Album>();
	
	public void addAlbum(Album a) {
		acervo.add(a);	
		System.out.println("Album adicionado (" +a.getNome()+")");
	}
	
	public ArrayList<Album> todosOsAlbuns(){
		return this.acervo;
	}
}