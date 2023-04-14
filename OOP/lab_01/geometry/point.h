#ifndef POINT_H
#define POINT_H

#include <cstdio>
#include <cstdlib>
#include <cmath>

#include "action_data.h"
#include "errors.h"

struct point
{
    double x;
    double y;
    double z;
};

using point_t = struct point;

void point_default(point_t &point);

error_t fread_point(point_t &point, FILE *fin);

void move_point(point_t &point, const move_t &move);

void rotate_point(point_t &point, const point_t &r_center, const rotate_t &rotate);

void add_point(point_t &point, const point_t &r_center);

void sub_point(point_t &point, const point_t &r_center);

void scale_point(point_t &point, const point_t &s_center, const scale_t &scale);

void scale_point_about_origin(point_t &point, const scale_t &scale);

double to_radians(const double angle);

double create_r_cos(double angle);

double create_r_sin(double angle);

error_t save_point(const point_t &point, FILE *fout);

#endif // POINT_H
