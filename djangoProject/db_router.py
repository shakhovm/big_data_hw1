class DatabaseRouter(object):
    def module_switch(self, model):

        result = 'default'

        if model.__module__.startswith('cassandra'):
            result = 'cassandra'
        # if model.__module__.endswith('bar_db2_models'): result = 'bar'
        # if model.__module__.endswith('baz_models'): result = 'baz'
        # if model.__module__.endswith('grid_models'): result = 'grid'
        # #print 'here', model.__module__, result, model.__class__.__name__
        return result

    def db_for_read(self, model, **hints):
        return self.module_switch(model)

    def db_for_write(self, model, **hints):
        return self.module_switch(model)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.
        """
        # db_list = ('master', 'slave1', 'slave2')
        # if obj1._state.db in db_list and obj2._state.db in db_list:
        #     return True
        return None

    def allow_migrate(self, db, app_label, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True