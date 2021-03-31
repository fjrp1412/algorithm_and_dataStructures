class Node {
	constructor(value = null) {
		this._value = value;
		this._nextNode = null;
	}

	get value() {
		return this._value;
	}

	set value(value) {
		this._value = value;
	}

	get nextNode() {
		return this._nextNode;
	}

	set nextNode(node) {
		this._nextNode = node;
	}
}

class LinkedList {
	constructor(value = null) {
		this._head = new Node(value);
	}

	showList() {
		let result = "";
		let actual = this._head;
		while (actual.nextNode !== null) {
			result += `${actual.value} `;
		}
		console.log(result);
	}

	pushFront(value) {
		if (this._head.value === null) {
			this._head.value = value;
		}
		let node = new Node(value);
		node.nextNode = this._head;
		this._head = node;
	}

	getFront() {
		return this._head.value;
	}

	popFront() {
		if (this._head.value === null) {
			return null;
		}
		let node = new Node(value);
		let value = this._head.value;
		node.nextNode = this._head.nextNode;
		this._head = node;

		return value;
	}

	pushBack(value) {
		if (this._head.value === null) {
			this._head.value = value;
		}
		let actual = this._head;

		while (actual.nextNode !== null) {
			actual = actual.nextNode;
		}
		actual.nextNode = new Node(value);
	}

	getBack() {
		let actual = this._head;
		while (actual.nextNode !== null) {
			actual = actual.nextNode;
		}
		return actual.value;
	}

	popBack() {
		if (this._head.value === null) {
			return null;
		}
		let actual = this._head;
		while (actual.nextNode.nextNode !== null) {
			actual = actual.nextNode;
		}
		let value = actual.nextNode.value;
		actual.nextNode = null;
		return value;
	}

	find(value) {
		let actual = this._head;
		while (actual.nextNode !== null && actual.value !== value) {
			actual = actual.nextNode;
		}
		return actual.value === value;
	}
}
