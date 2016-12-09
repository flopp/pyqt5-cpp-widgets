#pragma once

#include <QWidget>
class QLabel;

class Widget: public QWidget 
{
    Q_OBJECT
    
    public:
        explicit Widget(QWidget* parent = nullptr);
        virtual ~Widget() {}
    
    public slots:
        void setText(const QString& s);
    
    private:
        QLabel* label = nullptr;
};
