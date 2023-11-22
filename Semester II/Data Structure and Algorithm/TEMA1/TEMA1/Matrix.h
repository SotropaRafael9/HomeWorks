#pragma once
#include <tuple>
#include <algorithm>
//DO NOT CHANGE THIS PART
typedef int TElem;
#define NULL_TELEM 0

class Matrix {

private:
	//TODO - Representation
	int nr_lines;
	int nr_columns;

	int capacity, size;
	std::tuple<int, int, TElem> *values; // line coloumn value
	
	void add_value(int i, int j, TElem value);
	void resize(int new_capacity);
	bool compare_elements(std::tuple<int, int, TElem>a, std::tuple<int, int, TElem>b);
public:
	//constructor
	Matrix(int nrLines, int nrCols);

	//returns the number of lines
	int nrLines() const;

	//returns the number of columns
	int nrColumns() const;

	//returns the element from line i and column j (indexing starts from 0)
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem element(int i, int j) const;

	//modifies the value from line i and column j
	//returns the previous value from the position
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem modify(int i, int j, TElem e);

	void setElemsOnLine(int line, TElem elem);

};
