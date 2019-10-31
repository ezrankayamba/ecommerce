'use stri ct';

const e = React.createElement;
class MainCart extends React.Component {
    constructor(props) {
        super(props);
        this.state = { products: [] };
    }

    addToCart(prod) {
        console.log(prod)
        let found = false
        let tmpProds = this.state.products
        for (let i = 0; i < tmpProds.length; i++) {
            let p = tmpProds[i]
            if (p.id === prod.id) {
                tmpProds[i] = { id: prod.id, count: prod.count }
                found = true
                break;
            }
        }
        if (!found) {
            tmpProds.push({ id: prod.id, count: prod.count })
        }
        this.setState({ products: tmpProds })
    }

    render() {
        let map = this.state.products.map(p => p.count)
        console.log(map)
        let t = map.reduce((a, b) => a + b, 0)
        console.log(t)
        return e('span', {}, t)
    }
}
let mainCartDiv = document.querySelector('.cart-counter')
const mainCart = ReactDOM.render(e(MainCart, {}), mainCartDiv)
class ProductCart extends React.Component {
    constructor(props) {
        super(props);
        this.state = { id: props.id, cart: 0 };
    }

    render() {
        return e(
            'a', {
                onClick: () => {
                    let count = this.state.cart + 1
                    console.log('Cart: ', this.state.id, ' - ', count)
                    this.setState({ cart: count })
                    mainCart.addToCart({ id: this.state.id, count: count })
                },
                className: 'btn pt-0 pb-0',
                role: 'button'
            },
            e('i', {
                className: 'fas fa-cart-plus'
            })
        );
    }
}

const list = document.querySelectorAll('.cart-btn-wrap')
list.forEach((el) => {
    ReactDOM.render(e(ProductCart, { id: el.dataset.id }), el);
})