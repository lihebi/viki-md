# Buffer tmp for viki articles.

```java
/*
* Section A. Import libraries
*/
import java.io.File;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

class Dom_Demo {

	public static void main(String args[])
	throws SAXException, IOException, ParserConfigurationException{
		/*
		* Section C. Initialize and build Document from a xml file
		*/

		File auctionFile = new File ("auctions.xml");

		long time =System.currentTimeMillis();
		Document queryDoc =
		DocumentBuilderFactory.newInstance()
		.newDocumentBuilder()
		.parse(auctionFile);


		NodeList openAuctions = queryDoc.getElementsByTagName("open_auctions");
		Node auctions = openAuctions.item(0);
		Node auction = auctions.getFirstChild();
		while(auction != null) {
			Node node = auction.getFirstChild();
			Double bid = Double.parseDouble(node.getFirstChild().getTextContent());
			String buyerId = "";
			node = node.getNextSibling();
			while(node.getNodeName() == "bidder") {
				System.out.println("bidder");
				// bid += Double.parseDouble(node.getLast)
				Node tmpNode = node.getFirstChild();
				while(tmpNode.getNodeName() != "personref") tmpNode = tmpNode.getNextSibling();
				buyerId = tmpNode.getAttributes().getNamedItem("person").getTextContent();
				bid += Double.parseDouble( tmpNode.getNextSibling().getFirstChild().getTextContent());
				node = node.getNextSibling();
			}
			System.out.println(bid);
			System.out.println(buyerId);
			while(node.getNodeName() != "seller") {
				node = node.getNextSibling();
			}
			String sellerId = node.getAttributes().getNamedItem("person").getTextContent();
			System.out.println(sellerId);
			break;
		}

// if(nodeList != null && nodeList.getLength() > 0){
// 	for (int j = 0; j < nodeList.getLength(); j++) {
// 		Element el = (org.w3c.dom.Element) nodeList.item(j);
// 		if (el.hasAttribute("type_id") && el.getAttribute("type_id").equals("4218")) {
// 			type_id = Integer.parseInt(el.getAttribute("type_id"));
//
// 			System.out.println("type id:"+type_id);
// 		}
// 	}
// }

		// NodeList personList = queryDoc.getElementsByTagName("person");
		// Node person = personList.item(0);
		// while(person !=null)
		// {
		// 	Node name = person.getFirstChild();
		// 	if (name !=null)
		// 	System.out.println(name.getFirstChild().getNodeValue().trim());
		// 	person = (Element) person.getNextSibling();
		// }
		// System.out.println();
		// System.out.println("Time taken: "+(System.currentTimeMillis()-time));

}
}
```
