#include "ListIterator.h"
#include "IteratedList.h"
#include <exception>

ListIterator::ListIterator(const IteratedList& list) : list(list) {
	first();
}
//tetha(1)
void ListIterator::first() {
	current = list.root;
}
//tetha(1)
void ListIterator::next() {
//TODO - Implementation
	if (valid())
		current = current->next;
	else
		throw std::exception();
}
//tetha(1)
bool ListIterator::valid() const {
	
	return current != nullptr;
}
//tetha(1)
TElem ListIterator::getCurrent() const {
	//TODO - Implementation
	if (current == nullptr)
		throw std::exception();

	return current->value;
}



