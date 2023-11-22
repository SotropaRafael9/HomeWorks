#include "Map.h"
#include "MapIterator.h"

Map::Map() {
	//TODO - Implementation
	this->capacity = 100;
	this->Nodes = new Node[this->capacity];
	this->length = 0;
	this->head = -1;

	/// initialise the list with empty positions
	this->firstEmpty = 0;
	for (int i = 0; i < this->capacity - 1; i++) {
		this->Nodes[i].next = i + 1;
		this->Nodes[i].element = NULL_TELEM;
	}

	this->Nodes[this->capacity - 1].next = -1;
	this->Nodes[this->capacity - 1].element = NULL_TELEM;

}

// theta(1)
Map::~Map() {
	delete[] this->Nodes;
}

//theta(n)
TValue Map::add(TKey c, TValue v){
	//TODO - Implementation
	
	/// if the key already exists, replace its value
	int current = this->head;
	while (current != -1) {
		if (this->Nodes[current].element.first == c) {
			TValue old = this->Nodes[current].element.second;
			this->Nodes[current].element.second = v;
			return old;
		}
		current = this->Nodes[current].next;
	}

	/// if the key does not exist, add it
	if (this->firstEmpty == -1) {
		/// resize the list
		Node* newNodes = new Node[this->capacity * 2];
		for (int i = 0; i < this->capacity; i++) {
			newNodes[i] = this->Nodes[i];
		}
		for (int i = this->capacity; i < this->capacity * 2 - 1; i++) {
			newNodes[i].next = i + 1;
			newNodes[i].element = NULL_TELEM;
		}
		newNodes[this->capacity * 2 - 1].next = -1;
		newNodes[this->capacity * 2 - 1].element = NULL_TELEM;
		delete[] this->Nodes;
		this->Nodes = newNodes;
		this->firstEmpty = this->capacity;
		this->capacity *= 2;
	}

	int newElem = this->firstEmpty;
	this->firstEmpty = this->Nodes[this->firstEmpty].next;
	this->Nodes[newElem].element.first = c;

	this->Nodes[newElem].element.second = v;
	this->Nodes[newElem].next = this->head;
	this->head = newElem;
	this->length++;
	return NULL_TVALUE;


}

//theta(n)-where n is number of elements from the list
TValue Map::search(TKey c) const{
	//TODO - Implementation
	int current = this->head;
	while (current != -1) {
		if (this->Nodes[current].element.first == c)
			return this->Nodes[current].element.second;
		current = Nodes[current].next;
	}
	return NULL_TVALUE;
}


//theta(n)- where n is number of elements from the list
TValue Map::remove(TKey c){
	//TODO - Implementation
	/// first search for the key and replace its value if it is found
	int current = this->head;
	int prev = -1;
	while (current != -1) {
		if (this->Nodes[current].element.first == c) {
			TValue old = this->Nodes[current].element.second;
			if (prev == -1) {
				this->head = this->Nodes[current].next;
			}
			else {
				this->Nodes[prev].next = this->Nodes[current].next;
			}
			this->Nodes[current].next = this->firstEmpty;
			this->firstEmpty = current;
			this->length--;
			return old;
		}
		prev = current;
		current = this->Nodes[current].next;
	}
	return NULL_TVALUE;
}
	



// theta(1)

int Map::size() const {
	//TODO - Implementation
	return this->length;
}
// theta(1)

bool Map::isEmpty() const{
	//TODO - Implementation
	if (this->size() == 0) // or this->head == -1
		return true;
	return false;
}
// theta(1)

MapIterator Map::iterator() const {
	return MapIterator(*this);
}


//theta(n)-where n is the length of the old array
void Map::resize_array()
{
	this->capacity = 2 * this->capacity;
	Node* new_array = new Node[this->capacity];

	/// copy the elements from the old to the new array
	for (int i = 0; i < this->length; i++)
		new_array[i] = this->Nodes[i];

	/// the left capacity - length positions are empty
	this->firstEmpty = this->length;
	new_array[firstEmpty].next = this->length + 1;
	new_array[firstEmpty].element = NULL_TELEM;

	for (int i = this->length + 1; i < this->capacity - 1; i++) {
		new_array[i].next = i + 1;
		new_array[i].element = NULL_TELEM;
	}
	new_array[this->capacity - 1].next = -1;
	new_array[this->capacity - 1].element = NULL_TELEM;

	delete[] this->Nodes;
	this->Nodes = new_array;


}
