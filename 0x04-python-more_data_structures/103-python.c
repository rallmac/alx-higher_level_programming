#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 * @p: pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	printf("  first 10 bytes: ");

	Py_ssize_t size = ((PyVarObject *)p)->ob_size;

	if (size > 10)
		size = 10;
	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
