# Twitter based PoliticalNetwork
## Network Graph of German politicans based on who they follow 
**About The Project**

This project draws a NetworkX diagram of a network of german politicans based on who they follow on twitter. Is the first step in developing a political stance prediction application for Twitter. 
In Twitter lingo, users an account follows are called their friends. As everyone knows, you can choose your friends, but not your followers. The friends of a Twitter account therefore constitute a way of positioning them inside their network, in this case politically.
Every account is coloured according to its corresponding party colors. The exception to this rule are persons of interest which are colored orange.

The data was extracted using the Twitter API, processed with Python 3.8 and visualized with NetworkX. The network diagram is solely based on the friends of the depicted accounts. Their positions in the diagram result from nodes repelling each other while edges pull them together (NetworkX spring layout). The size of a node depends on the number of incoming and outgoing edges/relations.
Nodes with few connections to the network are especially prone to changing position. For the vast majority of displayed politician accounts, this is no issue. Only persons of interest whose positions were stable over a number of chart generations are displayed on the images above.

**Libraries**
* pickle
* networkx
* matplotlib.pyplot
* pandas.io.sql
* psycopg2

**Files**

* core_friend_plot.pkl: Pickle file with actual values you can use the draw the network plot
* auswertung.py: Loads pickle file, draws networkx diagram
* db_operations.py: access to database which holds the the twitter data

**Usage**

Download files and run in Python 3.8.
Select auswertung.py and configure plot_friend_rel_edges().  
Here are examples for the function calls:

Examples for function calls:

    'plot_friend_rel_edges(faction = 0, get_data_from_DB=False, export=False)'
    'plot_friend_rel_edges(faction="FDP MDBs", get_data_from_DB=False, export=False)'
    'plot_friend_rel_edges(faction="Hans-Georg Maaßen", get_data_from_DB=False, export=False)'
    'plot_friend_rel_edges(faction="Katja Kipping", get_data_from_DB=False, export=False)'


Options for faction:

1. 0: Displays all edges 
2. 'Union MDBs': this parties edges only 
3. 'SPD MDBs'
4. 'AfD'
5. 'Linke MdBs'
6. 'Grüne MDBs'
7 'FDP MDBs'

get_data_from_DB
1. False: Load data from pickle file
2. True: Fetch data from DB. Will not work unless you have a DB with fitting data.

export
1. False: show diagram 
2. True: save diagram as .png


**Results**

The individual accounts cluster very nicely into their respective parties. However
nodes with few connections to the network are especially prone to changing position. 
There are other downsides to this approach:
* Newspapers and journalists can’t be placed properly in the diagram. For example, BILD and taz appear politically close (which they are not at all), since they follow accounts from all over the political spectrum.
* To follow an account does not necessarily mean one endorses its positions. One might just wan’t to stay on top of its deeds and misdeeds.
* The placement of the political parties and especially of accounts with few connections to the rest of the network are, to some degree, random. Refer to the section “technical” for details.