def get_app_list(self, request):
    app_dict = self._build_app_dict(request)

    app_list = []

    for app_config in settings.ADMIN_REORDER:
        target_app_id = app_config.get('app')

        if target_app_id in app_dict:
            new_app = deepcopy(app_dict[target_app_id])
            new_app['models'] = []

            if 'label' in app_config:
                new_app['name'] = app_config.get('label')

            if 'models' in app_config:
                for model_config in app_config.get('models'):
                    model_app, model_name = model_config.get('model').split('.')

                    target_model = None
                    for model in app_dict[model_app]['models']:
                        if model['object_name'] == model_name:
                            target_model = deepcopy(model)

                    if target_model:
                        if 'label' in model_config:
                            target_model['name'] = model_config.get('label')

                        new_app['models'].append(target_model)

            app_list.append(new_app)

    return app_list


admin.AdminSite.get_app_list = get_app_list
