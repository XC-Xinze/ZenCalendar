function createTaskCard(task) {
  const card = document.createElement("div");

  const completedClass = task.is_completed ? "opacity-60" : "";
  const titleClass = task.is_completed
    ? "font-semibold text-stone-400 line-through"
    : "font-semibold text-on-surface";

  card.className = `bg-surface-container-lowest p-5 rounded-xl shadow-[0_4px_20px_rgba(138,114,108,0.04)] border-l-4 border-primary ${completedClass}`;

  card.innerHTML = `
    <div class="flex justify-between items-start mb-2">
      <span class="px-2.5 py-0.5 rounded-full bg-primary-fixed text-on-primary-fixed-variant text-[10px] font-bold uppercase tracking-wider">
        ${task.is_completed ? "Done" : "Task"}
      </span>
    </div>
    <h3 class="${titleClass} mb-1">${task.title}</h3>
    <p class="text-xs text-stone-500 leading-relaxed">Due: ${task.custom_date || "No date"}</p>
  `;

  return card;
}

async function handleAddTask() {
    const input = document.getElementById("task-input")
    if (!input) return;

    const title = input.value.trim()
    if (!title) return;

    try {
        const result = await window.apiBridge.createTask(title);

        if(!result.success) {
            alert(result.error || "1Faild to create");
            return;
        }

        input.value = "";
        await renderTasks();
    } catch(error) {
        console.error("Faild to create", error);
        alert("2Failed to create task")
    }
}

function bindTaskAddBtn() {
    const addBtn = document.getElementById("add-task-btn");
    const input = document.getElementById("task-input");

    if (addBtn) {
        addBtn.addEventListener("click",handleAddTask);
    }
    if (input) {
        input.addEventListener("keydown",async (event) => {
            if (event.key === "Enter") {
                await handleAddTask;
            }
        });
    }
}

async function renderTasks() {
  const root = document.getElementById("task-list-root");
  if (!root) return;

  root.innerHTML = "";

  try {
    const tasks = await window.apiBridge.getAllTasks();

    if (!tasks || tasks.length === 0) {
      root.innerHTML = `
        <div class="text-sm text-stone-400 italic">
          No tasks yet.
        </div>
      `;
      return;
    }

    tasks.forEach(task => {
      const card = createTaskCard(task);
      root.appendChild(card);
    });
  } catch (error) {
    console.error("Failed to load tasks:", error);
    root.innerHTML = `
      <div class="text-sm text-red-500">
        Failed to load tasks.
      </div>
    `;
  }
}

window.addEventListener("pywebviewready", () => {
  bindTaskAddBtn();
  renderTasks();
});