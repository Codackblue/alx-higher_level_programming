#include <stdio.h>
#include <Python.h>
#include <time.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_bytes - Prints bytes info
 * @p: Python Objects
 * Return: no return or void return
 */
void print_python_bytes(PyObject *p)
{
	char *fstr;
	long int size, f, flim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	fstr = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", fstr);

	if (size >= 10)
		flim = 10;
	else
		flim = size + 1;

	printf("  first %ld bytes:", flim);

	for (f = 0; f < flim; f++)
		if (fstr[f] >= 0)
			printf(" %02x", fstr[f]);
		else
			printf(" %02x", 256 + fstr[f]);

	printf("\n");
}

/**
 * print_python_list - Prints list info
 * @p: Python Objects
 * Return: no return or void
 */
void print_python_list(PyObject *p)
{
	long int size, f;
	PyListObject *flist;
	PyObject *fobj;

	size = ((PyVarObject *)(p))->ob_size;
	flist = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", flist->allocated);

	for (f = 0; f < size; f++)
	{
		fobj = ((PyListObject *)p)->ob_item[f];
		printf("Element %ld: %s\n", f, ((fobj)->ob_type)->tp_name);
		if (PyBytes_Check(fobj))
			print_python_bytes(fobj);
	}
}
