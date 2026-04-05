window.apiBridge = {
    async getAllTasks() {
        if (!window.pywebview || !window.pywebview.api) {
            throw new Error("pywebview is not ready");
        }
        return await window.pywebview.api.get_all_tasks();
    },
    async createTask(title) {
        if (!window.pywebview || !window.pywebview.api) {
            throw new Error("pywebview is not ready");
        }
        return await window.pywebview.api.create_task(title);
    }
};
