
#include <exception>
#include "ListIterator.h"
#include "IteratedList.h"

IteratedList::IteratedList() {
	//TODO - Implementation
}
//tetha(1) for all
int IteratedList::size() const {
	return list_size;
}
//tetha(1)
bool IteratedList::isEmpty() const {
	return list_size == 0;
}
//tetha(1)
ListIterator IteratedList::first() const {
	return ListIterator(*this);
}
//tetha(1)
TElem IteratedList::getElement(ListIterator pos) const {
	//TODO - Implementation
	if (!pos.valid())
		throw std::exception();
	return pos.current->value;
}
// removes the element from position pos
//returns the removed element
//after removal pos is positioned on the next element (the one after the removed one) or it is invalid if the last element was removed
//throws an exception if pos is not valid
//tetha(1) 
TElem IteratedList::remove(ListIterator& pos) {
	//TODO - Implementation
	if(!pos.valid())
		throw std::exception();
	list_size--;
	TElem value = pos.current->value;
	dll_node* theNext = pos.current->next;

	if (pos.current == root) // if at begining
	{
		dll_node* current = root;
		root = root->next;
		delete current;
		if(root != nullptr)
			root->prev = nullptr;
	}
	else if(pos.current->next == nullptr) //if at end
	{
		pos.current->prev->next = nullptr;
		delete pos.current;
	}
	else // if in middle
	{
		pos.current->prev->next = pos.current->next;
		pos.current->next->prev = pos.current->prev;
		delete pos.current;
	}
	//pos.current = pos.current->next;
	pos.current = theNext;
	return value;
}

//best case tetha(1)
//worst tetha(n)
//average

ListIterator IteratedList::search(TElem e) const{
	//TODO - Implementation
	ListIterator it = first();
	while (it.valid())
	{
		if (it.getCurrent() == e)
			return it;
		it.next();
	}
	return it;
	

}

// changes the element from the current position to the given one.
//returns the old value from the position
//throws exception if the position is not valid
//tetha(1)
TElem IteratedList::setElement(ListIterator pos, TElem e) {
    //TODO - Implementation
	if (!pos.valid())
		throw std::exception();

	TElem value = pos.current->value;
	pos.current->value = e;
	return value;


}

// // adds a new element after the current element from the iterator
//after addition, pos points to the newly added element
//throws an exception if pos is not valid
//tetha(1)
void IteratedList::addToPosition(ListIterator& pos, TElem e) {
    //TODO - Implementation
	if (!pos.valid())
		throw std::exception();
	dll_node* var = new dll_node();
	var->value = e;
	if (pos.current == root && root->next == nullptr) // add to begin (only one element)
	{
		var->next = root->next;
		root->next = var;
		var->prev = root;
	}
	else if (pos.current->next == nullptr) // add to end
	{
		var->prev = pos.current;
		pos.current->next = var;
	}
	else // add to middle
	{
		var->prev = pos.current;
		var->next = pos.current->next;
		var->prev->next = var;
		var->next->prev = var;
	}
	list_size++;
	pos.current = pos.current->next;


}
//best case tetha(n)
//worst case tetha(n)

void IteratedList::addToEnd(TElem e) {
	list_size++;
	if (root == nullptr)
	{
		root = new dll_node();
		root->value = e;
		return;
	}
	dll_node* current_node = root;
	while (current_node->next != nullptr)
		current_node = current_node->next;
	dll_node* new_end = new dll_node();
	new_end->value = e;
	current_node->next = new_end;
	new_end->prev = current_node;
	new_end->next = nullptr;
}

//tetha(1)
void IteratedList::addToBeginning(TElem e)
{
	list_size++;
	if (root == nullptr)
	{
		root = new dll_node();
		root->value = e;
		return;
	}
	dll_node* new_element = new dll_node();
	new_element->value = e;
	new_element->next = root;
	root->prev = new_element;
	root = new_element;

}
void IteratedList::filter(Condition cond)
{

	ListIterator it = first();
	while (it.valid())
	{
		if (cond(it.getCurrent()) == false)
		{
			remove(it);
		}
		else
		{
			it.next();
		}

	}

}
IteratedList::~IteratedList() {
	//TODO - Implementation
}
