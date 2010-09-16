#ifndef SUGARCLIENT_H
#define SUGARCLIENT_H

#include "ui_mainwindow.h"
#include <detailswidget.h>
#include <accountspage.h>
#include <opportunitiespage.h>
#include <leadspage.h>
#include <contactspage.h>
#include <campaignspage.h>
#include "enums.h"

#include <QMainWindow>

class QAction;
class QComboBox;
class QProgressBar;
class QTimer;
class QToolBar;

namespace Akonadi {
    class AgentInstance;
}

class SugarClient : public QMainWindow
{
    Q_OBJECT
public:
    SugarClient();

    ~SugarClient();

    inline void displayDockWidgets( bool value = true )
    { mUi.showDetails->setChecked( value ); }
    DetailsWidget *detailsWidget( DetailsType type );

Q_SIGNALS:
    void resourceSelected( const QByteArray &identifier );
    void displayDetails();

protected:
    void closeEvent( QCloseEvent *event );

private:
    void initialize();
    void createMenus();
    void createToolBar();
    void createDockWidgets();
    void setupActions();
    void createTabs();

    QMenu *mViewMenu;
    QToolBar *mToolBar;
    QDockWidget *mAccountDetailsDock;
    DetailsWidget *mAccountDetailsWidget;
    QAction *mViewAccountAction;
    QDockWidget *mOpportunityDetailsDock;
    DetailsWidget *mOpportunityDetailsWidget;
    QAction *mViewOpportunityAction;
    QDockWidget *mLeadDetailsDock;
    DetailsWidget *mLeadDetailsWidget;
    QAction *mViewLeadAction;
    QDockWidget *mContactDetailsDock;
    DetailsWidget *mContactDetailsWidget;
    QAction *mViewContactAction;
    QDockWidget *mCampaignDetailsDock;
    DetailsWidget *mCampaignDetailsWidget;
    QAction *mViewCampaignAction;
    QList<Page*> mPages;

    QComboBox * mResourceSelector; // Login;

    Ui_MainWindow mUi;

    QProgressBar *mProgressBar;
    QTimer *mProgressBarHideTimer;

private Q_SLOTS:
    void slotDelayedInit();
    void slotReload();
    void slotResourceSelectionChanged( int index );
    void slotShowMessage( const QString& );
    void slotManageItemDetailsView( int currentTab );
    void slotManageDetailsDisplay( bool value );
    void slotDetailsDisplayDisabled( bool value );
    void slotLogin();
    void slotConfigureResources();
    void slotResourceError( const Akonadi::AgentInstance &resource, const QString &message );
    void slotResourceOnline( const Akonadi::AgentInstance &resource, bool online );
    void slotResourceProgress( const Akonadi::AgentInstance &resource );

private:
    void detachDockViews( bool value );
    QComboBox* getResourcesCombo();
    Akonadi::AgentInstance currentResource() const;
};

#endif
