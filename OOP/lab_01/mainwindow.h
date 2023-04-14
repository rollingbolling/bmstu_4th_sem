#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include "errors.h"
#include "actions.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    void on_actionSave_triggered();

    void on_actionLoad_triggered();

    void on_actionInfFile_triggered();

    void on_actionInfProgram_triggered();

    void on_actionInfDeveloper_triggered();

private slots:
    error_t draw();

    void on_buttonMoving_clicked();

    void on_buttonTurn_clicked();

    void on_buttonScale_clicked();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
