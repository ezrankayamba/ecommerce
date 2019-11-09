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
    // <div class="btn-group" role="group" aria-label="BuyOrCart">
    //                             <a role="button" href="#" class="btn btn-sm btn-outline-secondary"><i class="fas fa-cart-plus"></i> Cart</a>
    //                             <a role="button" href="#" class="btn btn-sm btn-secondary">Buy Now</a>
    //                         </div>
    render() {
        let rnd = e(
            'div', {
                className: 'btn-group',
                role: 'group'
            },
            [
                e(
                    'a', {
                        onClick: () => {
                            let count = this.state.cart + 1
                            console.log('Cart: ', this.state.id, ' - ', count)
                            this.setState({ cart: count })
                            mainCart.addToCart({ id: this.state.id, count: count })
                        },
                        role: 'button',
                        className: 'btn btn-sm btn-outline-secondary'
                    }, [
                        e('i', {
                            className: 'fas fa-cart-plus'
                        }),
                        ' Cart'
                    ]
                ),
                e(
                    'a', {
                        onClick: () => {
                            let count = this.state.cart + 1;
                            console.log('Cart: ', this.state.id, ' - ', count);
                            this.setState({ cart: count });
                            mainCart.addToCart({ id: this.state.id, count: count });
                            console.log('Buy Now');
                        },
                        role: 'button',
                        className: 'btn btn-sm btn-secondary text-primary'
                    }, 'Buy Now'
                )
            ]
        )
        // return e(
        //     'a', {
        //         onClick: () => {
        //             let count = this.state.cart + 1
        //             console.log('Cart: ', this.state.id, ' - ', count)
        //             this.setState({ cart: count })
        //             mainCart.addToCart({ id: this.state.id, count: count })
        //         },
        //         className: 'btn pt-0 pb-0',
        //         role: 'button'
        //     },
        //     e('i', {
        //         className: 'fas fa-cart-plus'
        //     })
        // );
        return rnd;
    }
}

const list = document.querySelectorAll('.cart-btn-wrap')
list.forEach((el) => {
    ReactDOM.render(e(ProductCart, { id: el.dataset.id }), el);
})