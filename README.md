This repository contains a paper and code to efficiently enumerate maximal cliques; in a
worst case of O(|V|^8) (Python code runs in roughly O(|V|^5)). Putting on github for a
record, paper exists and is being worked on to find only maximal cliques.

Problems \[Updated 23/04/24\]:
- To _only_ find maximal cliques, must iterate through all non-maximal cliques found. This
operation is expontential as there can be 3^(|V| / 3) maximal cliques.
- Proofs are first draft, could be logic errors

The fix for the expontential problem will require some tweaking and proofs of the common
edge definition, making it only work for maximal cliques. However, without the routine
that culls non-maximal cliques, the program will always still output maximal; just not
strictly.
