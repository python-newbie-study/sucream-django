function tmp() {
    alert("버튼이 눌렸습니다.")
}

Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>{{ todo.text }}</li>'
})

var app = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
        message: "Hello Vue.js!"
    },
});

var app2 = new Vue({
    el: "#app2",
    delimiters: ['[[', ']]'],
    data: {
        message: "Hello Vue.js!"
    },
    methods: {
        test: function () {
            this.message = this.message.split('').reverse().join('')
        }
    }
});

var app3 = new Vue({
    el: '#app3',
    data: {
      groceryList: [
        { id: 0, text: 'Vegetables' },
        { id: 1, text: 'Cheese' },
        { id: 2, text: 'Whatever else humans are supposed to eat' }
      ]
    }
})