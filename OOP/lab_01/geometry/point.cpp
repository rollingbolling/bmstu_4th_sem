#include "point.h"

double to_radians(const double angle) {
    return angle * (M_PI / 180);
}

double create_r_cos(double angle)
{
    return cos(to_radians(angle));
}

double create_r_sin(double angle)
{
    return sin(to_radians(angle));
}

static void rotate_xp(point_t &point, const double angle)
{
    double r_cos = create_r_cos(angle);
    double r_sin = create_r_sin(angle);
    double y = point.y;

    point.y = point.y * r_cos + point.z * r_sin;
    point.z = -y * r_sin + point.z * r_cos;
}

static void rotate_yp(point_t &point, const double angle)
{
    double r_cos = create_r_cos(angle);
    double r_sin = create_r_sin(angle);
    double x = point.x;

    point.x = point.x * r_cos + point.z * r_sin;
    point.z = -x * r_sin + point.z * r_cos;
}

static void rotate_zp(point_t &point, const double angle)
{
    double r_cos = create_r_cos(angle);
    double r_sin = create_r_sin(angle);
    double x = point.x;

    point.x = point.x * r_cos + point.y * r_sin;
    point.y = -x * r_sin + point.y * r_cos;
}

void add_point(point_t &point, const point_t &r_center)
{
    point.x += r_center.x;
    point.y += r_center.y;
    point.z += r_center.z;
}

void sub_point(point_t &point, const point_t &r_center)
{
    point.x -= r_center.x;
    point.y -= r_center.y;
    point.z -= r_center.z;
}

void point_default(point_t &point)
{
    point.x = 0.0;
    point.y = 0.0;
    point.z = 0.0;
}

error_t fread_point(point_t &point, FILE *fin)
{
    error_t rc = SUCCESS;
    if (fin == NULL)
        rc = FILE_OPEN_ERROR;
    else if(fscanf(fin, "%lf %lf %lf", &point.x, &point.y, &point.z) != 3)
        rc = READ_FILE_ERROR;

    return rc;
}

void move_point(point_t &point, const move_t &move)
{
    point.x += move.dx;
    point.y += move.dy;
    point.z += move.dz;
}

void rotate_point(point_t &point, const point_t &r_center, const rotate_t &rotate)
{
    add_point(point, r_center);
    rotate_xp(point, rotate.angle_x);
    rotate_yp(point, rotate.angle_y);
    rotate_zp(point, rotate.angle_z);
    sub_point(point, r_center);
}

void scale_point_about_origin(point_t &point, const scale_t &scale)
{
    point.x *= scale.kx;
    point.y *= scale.ky;
    point.z *= scale.kz;
}

void scale_point(point_t &point, const point_t &s_center, const scale_t &scale)
{
    add_point(point, s_center);
    scale_point_about_origin(point, scale);
    sub_point(point, s_center);
}

error_t save_point(const point_t &point, FILE *fout)
{
    if (fout == NULL)
        return FILE_OPEN_ERROR;
    int rc = fprintf(fout, "%lf %lf %lf\n", point.x,
                                            point.y,
                                            point.z);
    if (0 > rc)
        return FILE_WRITE_ERROR;
    return SUCCESS;
}
