#include <QLabel>
#include <QVBoxLayout>

#include "widget.h"

Widget::Widget(QWidget* parent) : 
    QWidget{parent},
    label{new QLabel(this)}
{ 
    auto layout = new QVBoxLayout(this);
    layout->addWidget(label);
}

void Widget::setText(const QString& s) 
{
    label->setText(s);
}
