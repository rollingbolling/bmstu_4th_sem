#include "edges.h"

error_t allocate_edges(edge_t **array, int size)
{
    error_t rc = SUCCESS;
    if (size <= 0)
        rc = SIZE_EDGES_ERROR;
    else
    {
        edge_t *temp_array = (edge_t *) malloc(size * sizeof(edge_t));
        if (!temp_array)
            rc = MEMORY_ALLOCATE_ERROR;
        else
        {
            if (*array)
                free(*array);
            *array= temp_array;
        }
    }
    return rc;
}

void edges_default(edges_t &edges)
{
    edges.array_edges = NULL;
    edges.size = 0;
}

void reset_edges(edges_t &edges)
{
    if (edges.array_edges)
        free(edges.array_edges);
    edges_default(edges);
}

error_t fread_edge(FILE *fin, edge_t &edge)
{
    error_t rc = SUCCESS;
    if (fin == NULL)
        rc = FILE_OPEN_ERROR;
    else if (fscanf(fin, "%d %d", &edge.first_point,
                           &edge.second_point) != 2)
        rc = READ_FILE_ERROR;

    return rc;
}

error_t fread_all_edges(edge_t *array, int size, FILE *fin)
{
    error_t rc = SUCCESS;
    if (fin == NULL)
        rc = FILE_OPEN_ERROR;
    else if (size <= 0)
        rc = SIZE_EDGES_ERROR;
    else if (!array)
        rc = MEMORY_ALLOCATE_ERROR;
    else
        for (int i = 0; rc == SUCCESS && i < size; i++)
            rc = fread_edge(fin, array[i]);

    return rc;
}

error_t fread_amount_edges(int &num_of_edges, FILE *fin)
{
    error_t rc = SUCCESS;
    if (fin == NULL)
        rc = FILE_OPEN_ERROR;
    else if (fscanf(fin, "%d", &num_of_edges) != 1)
        rc = READ_FILE_ERROR;
    else if (num_of_edges <= 0)
        rc = SIZE_POINTS_ERROR;

    return rc;
}

error_t fread_inf_about_edges(edges_t &edges, FILE *fin)
{
    if (fin == NULL)
        return FILE_OPEN_ERROR;

    error_t rc = SUCCESS;
    rc = fread_amount_edges(edges.size, fin);
    if (!rc)
    {
        rc = allocate_edges(&(edges.array_edges), edges.size);
        if (!rc)
        {
            rc = fread_all_edges(edges.array_edges, edges.size, fin);
            if (rc)
                reset_edges(edges);
        }
    }

    return rc;
}

error_t save_all_edges(const edges_t &edges, FILE *fout)
{
    error_t rc = SUCCESS;
    if (!edges.array_edges)
        rc = NOT_DATA_WRITE_ERROR;
    else if (0 > fprintf(fout, "%d\n", edges.size))
        rc = FILE_WRITE_ERROR;
    else
        for (int i = 0; rc == SUCCESS && i < edges.size; i++)
            rc = save_edge(edges.array_edges[i], fout);

    return rc;
}

error_t save_edge(const edge_t &edge, FILE *fout)
{
    int rc = fprintf(fout, "%d %d\n", edge.first_point, edge.second_point);
    if (0 > rc)
        return FILE_WRITE_ERROR;
    return SUCCESS;
}
