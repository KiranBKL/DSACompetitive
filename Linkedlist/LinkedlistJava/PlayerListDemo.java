import java.io.*;
import java.util.*;
class PlayerListDemo
{
	public static void main(String[] args) throws IOException
	{
		PlayerList pl=new PlayerList();
		FileReader fr=new FileReader("players.txt");
		BufferedReader br=new BufferedReader(fr);
		String line="";
		//StringTokenizer st=null;
		while((line=br.readLine())!=null)
		{
			StringTokenizer st=new StringTokenizer(line);
			String name=st.nextToken();
			int score=Integer.parseInt(st.nextToken());
			float avg=Float.parseFloat(st.nextToken());
			pl.add(name,score,avg);
		}
		br.close();
		fr.close();
		
		
			}
}
