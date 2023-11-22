#include "SortedBag.h"
#include "SortedBagIterator.h"

SortedBag::SortedBag(Relation r){
	//TODO - Implementation
	relation = r;
	rootIndex = -1;
	firstEmpty = 0;
	len = 0;

}

void SortedBag::add(TComp e) {
	//TODO - Implementation
	len++; 

	if (isEmpty())// If the bag is empty, add the element as the root
	{
		elements.push_back(Node(e, 1, -1, -1)); 
		rootIndex = 0; 
		firstEmpty = 1; 
	}
	else {
		int currentNode = rootIndex; 
		int parent = -1; 


		while (currentNode != -1) {
			parent = currentNode; // Update the parent index
			if (elements[currentNode].element == e) {
				elements[currentNode].frequency++; // Increase the frequency if the element already exists
				return;
			}
			else if (relation(e, elements[currentNode].element))
				currentNode = elements[currentNode].leftChildIndex; // Move to the left child if the element is smaller
			else
				currentNode = elements[currentNode].rightChildIndex; // Move to the right child
		}

		// Add the new element at the appropriate position
		if (relation(e, elements[parent].element))
			elements[parent].leftChildIndex = firstEmpty; 
		else
			elements[parent].rightChildIndex = firstEmpty; 

		elements.push_back(Node(e, 1, -1, -1)); // Add the new node to the elements array

		firstEmpty++; 
	}

}



bool SortedBag::remove(TComp e) {
	//TODO - Implementation
	
		int currentNode = rootIndex; // Index of the current node (start with the root)
		int parent = -1; // Index of the parent node (initialized as -1)

		// Search for the node with the element to be removed
		while (currentNode != -1) { //goes until the current node becomes -1 or founds an element
			if (elements[currentNode].element == e)
				break; 
			else if (relation(e, elements[currentNode].element)) {
				parent = currentNode; 
				currentNode = elements[currentNode].leftChildIndex; // Move to the left child if the element is smaller
			}
			else {
				parent = currentNode; // Update parent
				currentNode = elements[currentNode].rightChildIndex; // Move to the right child
			}
		}

		// Check if element was found
		if (currentNode == -1)
			return false; 
		else {
			// Check if element has multiple occurrences
			if (elements[currentNode].frequency > 1) {
				elements[currentNode].frequency--; 
				return true; // Element removed (frequency decreased), return true
			}
			else {
				// 
				// remove if it has no children
				if (elements[currentNode].leftChildIndex == -1 && elements[currentNode].rightChildIndex == -1) {
					if (parent == -1) {
						rootIndex = -1; 
						firstEmpty = 0; 
						len--; 
						return true; 
					}
					else {
						// Update appropriate child index of the parent node
						if (elements[parent].leftChildIndex == currentNode)
							elements[parent].leftChildIndex = -1;
						else
							elements[parent].rightChildIndex = -1;
					}
				}
				// Node with only a right child
				else if (elements[currentNode].leftChildIndex == -1) {
					if (parent == -1) {
						rootIndex = elements[currentNode].rightChildIndex; // Update root index
						firstEmpty = currentNode; // Update firstEmpty index
					}
					else {
						// Update appropriate child index of the parent node
						if (elements[parent].leftChildIndex == currentNode)
							elements[parent].leftChildIndex = elements[currentNode].rightChildIndex;
						else
							elements[parent].rightChildIndex = elements[currentNode].rightChildIndex;
					}
				}
				// Node with only a left child
				else if (elements[currentNode].rightChildIndex == -1) {
					if (parent == -1) {
						rootIndex = elements[currentNode].leftChildIndex; 
						firstEmpty = currentNode; 
					}
					else {
						// update appropriate child index of the parent node
						if (elements[parent].leftChildIndex == currentNode)
							elements[parent].leftChildIndex = elements[currentNode].leftChildIndex;
						else
							elements[parent].rightChildIndex = elements[currentNode].leftChildIndex;
					}
				}
				// Node with both left and right children
				else {
					// Find the successor (smallest element in the right subtree)
					int successor = elements[currentNode].rightChildIndex;
					int successorParent = currentNode;

					while (elements[successor].leftChildIndex != -1) {
						successorParent = successor; // Update successor's parent
						successor = elements[successor].leftChildIndex; 
						}

				// Update the element of the node to be removed
					elements[currentNode].element = elements[successor].element;
					elements[currentNode].frequency = elements[successor].frequency;

					// Update appropriate child index of the successor's parent
					if (elements[successorParent].leftChildIndex == successor)
						elements[successorParent].leftChildIndex = elements[successor].rightChildIndex;
					else
						elements[successorParent].rightChildIndex = elements[successor].rightChildIndex;

					// Update firstEmpty index
					firstEmpty = successor;
					}
				}
			len--;
			return true;
		}
}



//theta(n)

bool SortedBag::search(TComp elem) const {
	//TODO - Implementation
	int currentNode = rootIndex;
	while (currentNode != -1)
	{
		if (elements[currentNode].element == elem)
			return true;
		else if (relation(elem, elements[currentNode].element))
			currentNode = elements[currentNode].leftChildIndex;
		else
			currentNode = elements[currentNode].rightChildIndex;
	}
	return false;

}

//theta(nodes) = theta(n)
int SortedBag::nrOccurrences(TComp elem) const {
	//TODO - Implementation
	int currentNode = rootIndex;

	while (currentNode != -1)// Search for the node containing the element
	{
		if (elements[currentNode].element == elem)
			return elements[currentNode].frequency;
		else if (relation(elem, elements[currentNode].element)) //goes to the left child if the element is smaller than the current node
			currentNode = elements[currentNode].leftChildIndex;
		else
			currentNode = elements[currentNode].rightChildIndex;
	}
	return 0;
	
}


//thetha(size) = theta(n)
int SortedBag::size() const {
	int currentNode = rootIndex;
	int size = 0;
	for(int i = 0; i < elements.size(); i++)
		if (elements[i].frequency > 0)
			size += elements[i].frequency;
	return size;
}

//theta(1)
bool SortedBag::isEmpty() const {
	//TODO - Implementation
	return elements.size() == 0;
}

//theta(size) = theta(n)
int SortedBag::elementsWithThisFrequency(int frequency) const
{
	if (frequency <= 0)
		throw std::exception();
	int currentNode = rootIndex;
	int size = 0;
	for (int i = 0; i < elements.size(); i++)
		if (elements[i].frequency == frequency)
			size++;
	return size;
	
}


SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}


SortedBag::~SortedBag() {
}

