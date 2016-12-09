%Module Custom

%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip
%Import QtWidgets/QtWidgetsmod.sip

class Widget: QWidget 
{

%TypeHeaderCode
#include <custom/widget.h>
%End

public:
    explicit Widget(QWidget* parent = nullptr);
    virtual ~Widget();

public slots:
    void setText(const QString& s);
};
