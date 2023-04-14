#include "points.h"

void points_default(points_t &points)
{
    points.array_points = NULL;
    points.size = 0;
}

error_t allocate_points(point_t **array, int size)
{
    error_t rc = SUCCESS;
    if (size <= 0)
        rc = SIZE_POINTS_ERROR;
    else
    {
        point_t *temp_array = (point_t *) malloc(size * sizeof(point_t));
        if (!temp_array)
            rc = MEMORY_ALLOCATE_ERROR;
        else
        {
            if (*array)
                free(*array);
            *array = temp_array;
        }
    }

    return rc;
}

void reset_points(points_t &points)
{
    if (points.array_points)
        free(points.array_points);
    points_default(points);
}

error_t fread_inf_about_points(points &points, FILE *fin)
{
    if (fin == NULL)
        return FILE_OPEN_ERROR;

    error_t rc = fread_amount_points(points.size, fin);
    if (!rc)
    {
        rc = allocate_points(&(points.array_points), points.size);
        if (!rc)
        {
            rc = fread_all_points(points.array_points, points.size, fin);
            if (rc)
                free(points.array_points);
        }
    }
    return rc;
}

error_t fread_amount_points(int &number_of_points, FILE *fin)
{
    error_t rc = SUCCESS;
    if (fin == NULL)
        rc = FILE_OPEN_ERROR;
    else if (fscanf(fin, "%d", &number_of_points) != 1)
        rc = READ_FILE_ERROR;
    else if (number_of_points <= 0)
        rc = SIZE_POINTS_ERROR;

    return rc;
}

error_t fread_all_points(point_t *array, int size, FILE *fin)
{
    error_t rc = SUCCESS;
    if (fin == NULL)
        rc = FILE_OPEN_ERROR;
    else if (size <= 0)
        rc = SIZE_POINTS_ERROR;
    else if (!array)
        rc = MEMORY_ALLOCATE_ERROR;
    else
        for (int i = 0; rc == SUCCESS && i < size; i++)
            rc = fread_point(array[i], fin);

    return rc;
}

error_t move_all_points(points_t &points, const move_t &coeff)
{
    if (!points.array_points)
        return FIGURE_NOT_LOADED;

    for (int i = 0; i < points.size; i++)
        move_point(points.array_points[i], coeff);

    return SUCCESS;
}

error_t rotate_all_points(points_t &points, const point_t &r_center, const rotate_t &coeff)
{
    if (!points.array_points)
        return FIGURE_NOT_LOADED;

    for (int i = 0; i < points.size; i++)
        rotate_point(points.array_points[i], r_center, coeff);

    return SUCCESS;
}

error_t scale_all_points(points_t &points, const point_t &s_center, const scale_t &coeff)
{
    error_t rc = SUCCESS;
    if (!points.array_points)
        rc = FIGURE_NOT_LOADED;
    else if (coeff.kx == 0 || coeff.ky == 0 || coeff.kz == 0)
        rc = COEFF_SCALE_ERROR;
    else
        for (int i = 0; i < points.size; i++)
            scale_point(points.array_points[i], s_center, coeff);

    return rc;
}

error_t save_all_points(const points_t &points, FILE *fout)
{
    error_t rc = SUCCESS;
    if (!points.array_points)
        rc = NOT_DATA_WRITE_ERROR;
    else if (0 > fprintf(fout, "%d\n", points.size))
        rc = FILE_WRITE_ERROR;
    else
        for (int i = 0; rc == SUCCESS && i < points.size; i++)
            rc = save_point(points.array_points[i], fout);

    return rc;
}
