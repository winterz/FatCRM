#ifndef SALESFORCERESOURCE_H
#define SALESFORCERESOURCE_H

#include <akonadi/resourcebase.h>

class ModuleHandler;
class KDSoapMessage;
class SforceService;

class TNS__DeleteResponse;
class TNS__LoginResponse;
class TNS__QueryMoreResponse;
class TNS__QueryResponse;
class TNS__UpsertResponse;

template <typename U, typename V> class QHash;

class SalesforceResource : public Akonadi::ResourceBase, public Akonadi::AgentBase::Observer
{
    Q_OBJECT

public:
    SalesforceResource( const QString &id );
    ~SalesforceResource();

public Q_SLOTS:
    virtual void configure( WId windowId );

protected:
    SforceService* mSoap;

    QString mSessionId;

    Akonadi::Item mPendingItem;

    typedef QHash<QString, ModuleHandler*> ModuleHandlerHash;
    ModuleHandlerHash *mModuleHandlers;

protected:
    void aboutToQuit();
    void doSetOnline( bool online );

    void doLogin();

    void itemAdded( const Akonadi::Item &item, const Akonadi::Collection &collection );
    void itemChanged( const Akonadi::Item &item, const QSet<QByteArray> &parts );
    void itemRemoved( const Akonadi::Item &item );

    void connectSoapProxy();

protected Q_SLOTS:
    void retrieveCollections();
    void retrieveItems( const Akonadi::Collection &col );
    bool retrieveItem( const Akonadi::Item &item, const QSet<QByteArray> &parts );

    void loginDone( const TNS__LoginResponse &callResult );
    void loginError( const KDSoapMessage &fault );

#if 0
    void getAvailableModulesDone( const TNS__Module_list &callResult );
    void getAvailableModulesError( const KDSoapMessage &fault );
#endif

    void getEntryListDone( const TNS__QueryResponse &callResult );
    void getEntryListDone( const TNS__QueryMoreResponse &callResult );
    void getEntryListError( const KDSoapMessage &fault );

    void setEntryDone( const TNS__UpsertResponse &callResult );
    void setEntryError( const KDSoapMessage &fault );

    void deleteEntryDone( const TNS__DeleteResponse &callResult );
    void deleteEntryError( const KDSoapMessage &fault );
};

#endif
