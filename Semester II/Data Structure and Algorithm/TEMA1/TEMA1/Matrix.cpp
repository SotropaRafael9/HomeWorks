#include "Matrix.h"
#include <exception>
using namespace std;


Matrix::Matrix(int nrLines, int nrCols) {
	   
	//TODO - Implementation
	this->nr_lines = nrLines;
	this->nr_columns = nrCols;
	this->capacity = 2;
	this->values = new std::tuple<int, int, TElem>[capacity];
	size = 0;
}

int Matrix::nrLines() const {
	return this->nr_lines;
}


int Matrix::nrColumns() const {
	return this->nr_columns;
}

//Theta(n)-> size of the matrix - constant value
TElem Matrix::element(int i, int j) const {
	//TODO - Implementation
	// serach in the matrix for an element and if it finds it , it will retrun it if not return null
	if (i < 0 || j < 0 || i >= nr_lines || j >= nr_columns)
		throw std::exception();
	for (int index = 0; index < size; index++) 
		if (std::get<0>(values[index]) == i && std::get<1>(values[index]) == j)
			return std::get<2>(values[index]);
	return NULL_TELEM;

}
//Theta(size) 
void Matrix::resize(int new_capacity)
{
	std::tuple<int, int, TElem>* new_value = new std::tuple<int, int, TElem>[new_capacity];
	for (int index = 0; index < size; index++)
		new_value[index] = values[index];
	delete[] values;
	values = new_value;
	capacity = new_capacity;
}

// O(1) -canstant value
//compares to elements from tuple(matrix) and verify if it's in the lexicografic order
bool Matrix::compare_elements(std::tuple<int, int, TElem>a, std::tuple<int, int, TElem>b) {
	int line_a = std::get<0>(a); // 
	int line_b = std::get<0>(b);
	int column_a = std::get<1>(a);
	int column_b = std::get<1>(b);
	return line_a > line_b || (line_a == line_b && column_a > column_b);
}

// Theta (n) best avr worst
void Matrix::add_value(int i, int j, int e)
{
	std::tuple<int, int, TElem> val = std::make_tuple(i, j, e);
	if (compare_elements(values[0], val))
	{
		size++;
		if (size == capacity)
			resize(2 * capacity);
		for (int jndex = size; jndex > 0; jndex--)
			values[jndex] = values[jndex - 1];
		values[0] = val;
	}

	for (int index = 0; index < size - 1; index++)
	{
		if (compare_elements(val, values[index]) && compare_elements(values[index + 1], val)) {
			for (int jndex = size; jndex > index; jndex--)
				values[jndex] = values[jndex - 1];
			size++;
			values[index + 1] = val;
			if (size == capacity)
				resize(2 * capacity);
			return;
		}

	}
	values[size++] = val;
	if (size == capacity)
		resize(2 * capacity);
}
//theta(n)
//search for the element in the matrix and if it find it, return it and if not throw exception
TElem Matrix::modify(int i, int j, TElem e) {
	//TODO - Implementation
	if (i < 0 || j < 0 || i >= nr_lines || j >= nr_columns )
		throw std::exception();
	for (int index = 0; index < size; index++)
		if (std::get<0>(values[index]) == i && std::get<1>(values[index]) == j) {
			TElem old_value = std::get<2>(values[index]);
			values[index] = std::make_tuple(i, j, e);
			return old_value;
		}
	add_value(i, j, e);
	return NULL_TELEM;
}
//thetha(n^2)
void Matrix::setElemsOnLine(int line, TElem elem)
{
	if (line <0 || line > nr_lines)
		throw std::exception();
	for (int index = 0; index < nr_columns; index++)
	{
		//if (std::get<0>(values[index]) == line)
		//	std::get<2>(values[index]) = elem;
		Matrix::modify(line, index, elem);
	}
}

