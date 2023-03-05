package albumsoap;

public class Album {
	private String nome;
	private String ano;
	private String produtora;
	
	public Album(String n, String a, String p) {
		this.nome = n;
		this.ano = a;
		this.produtora = p;		
	}

	public Album ( ) {
		
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getAno() {
		return ano;
	}
	public void setAno(String ano) {
		this.ano = ano;
	}
	public String getProdutora() {
		return produtora;
	}
	public void setProdutora(String produtora) {
		this.produtora = produtora;
	}
	
}