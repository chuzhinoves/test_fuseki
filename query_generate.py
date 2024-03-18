def new_node_query(nodeID):
    query = '''
                PREFIX dc: <http://purl.org/dc/elements/1.1/>
                PREFIX ex: <http://example/>
                INSERT DATA
                { 
                ex:book%s dc:title "A new book%s";
                        dc:creator "A.N.Other%s" .
                }
                '''% (nodeID, nodeID, nodeID)
    return query 

def new_edge_query(nodeID1, nodeID2):
    query = '''
                PREFIX dc: <http://purl.org/dc/elements/1.1/>
                PREFIX ex: <http://example/>
                INSERT DATA
                { 
                    ex:book%s ex:link ex:book%s.
                }
                '''% (nodeID1, nodeID2)
    return query 

def new_complex_query(nodeID, neighbors : list):
    query = '''
                PREFIX dc: <http://purl.org/dc/elements/1.1/>
                PREFIX ex: <http://example/>
                INSERT DATA
                {
            '''
    query += """
                    ex:book%s dc:title "A new book%s";
                              dc:creator "A.N.Other%s" ."""%(nodeID, nodeID, nodeID)
    for neighbor in neighbors:
        query += """
                    ex:book%s ex:link ex:book%s.""" %(nodeID, neighbor)
    query += """
                }\n"""
    return query

if __name__== "__main__":
    print(new_complex_query(1, [2,3]))