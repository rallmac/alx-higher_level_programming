#include "Python.h"

/**
 * print_python_string - Prints information about Python strings
 * @p: A PyObject string object
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [Error] Invalid String Object\n");
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		print(" type: compact unicode object\n");
	printf(" length: %id\n", length);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
