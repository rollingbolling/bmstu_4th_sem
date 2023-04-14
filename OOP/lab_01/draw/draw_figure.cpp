#include "draw_figure.h"

point_t conversion(point_t point, const drawview_t &view)
{
    point.x += view.width / 2;
    point.y += view.height / 2;

    return point;
}

line_t get_points(const drawview_t &view, const edge_t &edge, const point_t *array_points)
{
    line_t line;

    line.first_point = conversion(array_points[edge.first_point], view);
    line.second_point = conversion(array_points[edge.second_point], view);

    return line;
}

error_t clear_scene(const drawview_t &view)
{
    if (!view.scene)
        return SCENE_WRONG_ERROR;

    view.scene->clear();
    return SUCCESS;
}

error_t draw_line(const drawview_t &view, const edge_t edge, const points_t &points)
{
    if (!view.scene)
        return SCENE_WRONG_ERROR;

    bool lower_check = edge.first_point >= 0 && edge.second_point >= 0;
    bool upper_check = edge.first_point < points.size && edge.second_point < points.size;

    if (points.size <= 0 || !lower_check || !upper_check)
        return INCORRECT_POINT_ID;

    line_t line = get_points(view, edge, points.array_points);

    view.scene->addLine(line.first_point.x, line.first_point.y, line.second_point.x, line.second_point.y);
    return SUCCESS;
}

error_t draw_lines(const drawview_t &view, const points_t &points, const edges_t &edges)
{
    error_t rc = SUCCESS;
    if (points.array_points == NULL || edges.array_edges == NULL)
        rc = MEMORY_ALLOCATE_ERROR;
    else if (!view.scene)
        rc = SCENE_WRONG_ERROR;
    else
    {
        for (int i = 0; rc == SUCCESS && i < edges.size; i++)
        {
            rc = draw_line(view, edges.array_edges[i], points);
        }
    }

    return rc;
}

error_t draw_figure(const figure_t &figure, drawview_t &view)
{
    error_t rc = clear_scene(view);
    if (!rc)
        rc = draw_lines(view, figure.points, figure.edges);

    return rc;
}
