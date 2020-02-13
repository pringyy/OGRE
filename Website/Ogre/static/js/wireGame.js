"use strict";
var n, t, r = function(n, t) {
        var r = document.createElement("canvas");
        return r.width = n, r.height = t, [r, r.getContext("2d")]
    },
    o = function() {
        var o = N();
        return {
            t: function(i, u, a) {
                var e, c = r(1280, 720),
                    f = c[0],
                    s = c[1],
                    v = hn(),
                    l = cn(f),
                    d = vn(u),
                    h = ln(),
                    p = function() {
                        e(), l.o(), v.o(), document.body.style.cursor = "default"
                    },
                    y = Mn(function() {
                        p(), a()
                    }),
                    M = sn(l);
                v.i(d), v.i(y), v.i(h), v.i(M), i.u.forEach(function(n) {
                    var r = {
                        s: {
                            x: n[0],
                            y: n[1]
                        },
                        v: {
                            size: n[2],
                            type: t.v
                        },
                        l: {
                            type: t.v
                        }
                    };
                    v.h(r)
                }), i.p.forEach(function(n) {
                    var r = {
                        s: {
                            x: n[0],
                            y: n[1]
                        },
                        M: {
                            size: n[2]
                        },
                        l: {
                            type: t.M
                        }
                    };
                    v.h(r)
                }), i.m.forEach(function(n) {
                    var r = {
                        s: {
                            x: n[0],
                            y: n[1]
                        },
                        v: {
                            size: n[2],
                            type: t.k
                        },
                        l: {
                            type: t.k
                        }
                    };
                    v.h(r)
                });
                var b = {
                        s: {
                            x: i.start[0],
                            y: i.start[1]
                        },
                        v: {
                            size: 0,
                            type: t.start
                        },
                        l: {
                            type: t.start
                        }
                    },
                    m = {
                        s: {
                            x: i.end[0],
                            y: i.end[1]
                        },
                        v: {
                            size: 0,
                            type: t.end
                        },
                        l: {
                            type: t.end
                        },
                        g: {
                            size: 30
                        }
                    },
                    k = {
                        A: {
                            attachments: [{
                                B: b,
                                D: n.left
                            }, {
                                B: m,
                                D: n.left
                            }]
                        }
                    },
                    x = {
                        finish: {},
                        l: {
                            type: t.finish
                        },
                        s: {
                            x: i.finish[0],
                            y: i.finish[1]
                        }
                    };
                v.h(b), v.h(x), v.h(m), v.h(k);
                return e = mn(function(n) {
                    ! function(n) {
                        M.update(n), y.update(n)
                    }(n),
                    function(n) {
                        s.drawImage(o, 0, 0), h.l(s, n), d.l(s, n)
                    }(n)
                }), {
                    canvas: f,
                    o: p
                }
            }
        }
    },
    i = function(n, t, r) {
        return n < t ? t : n > r ? r : n
    },
    u = function(n, t, r, o) {
        var i = t.x - n.x,
            u = t.y - n.y,
            a = ((r.x - n.x) * i + (r.y - n.y) * u) / (u * u + i * i);
        return (a >= 0 && a <= 1 ? Math.pow(n.x + i * a - r.x, 2) + Math.pow(n.y + u * a - r.y, 2) : a < 0 ? Math.pow(n.x - r.x, 2) + Math.pow(n.y - r.y, 2) : Math.pow(t.x - r.x, 2) + Math.pow(t.y - r.y, 2)) < o * o
    },
    a = function(n, t) {
        return Math.pow(n.x - t.x, 2) + Math.pow(n.y - t.y, 2)
    },
    e = function(n, t, r, o) {
        var i = (n.x - r.x) * (n.x - r.x) + (n.y - r.y) * (n.y - r.y);
        if (i <= (t - o) * (t - o)) return [];
        for (var u = Math.sqrt(i), a = (r.x - n.x) / u, e = (r.y - n.y) / u, c = [], f = 0, s = 1; s >= -1; s -= 2) {
            var v = (t - s * o) / u;
            if (!(v * v > 1))
                for (var l = Math.sqrt(Math.max(0, 1 - v * v)), d = 1; d >= -1; d -= 2) {
                    var h = a * v - d * l * e,
                        p = e * v + d * l * a;
                    c[f] = [];
                    var y = c[f] = new Array(2);
                    y[0] = {
                        x: n.x + t * h,
                        y: n.y + t * p
                    }, y[1] = {
                        x: r.x + s * o * h,
                        y: r.y + s * o * p
                    }, f++
                }
        }
        return c
    },
    c = function(n) {
        return (n % 1 + 1) % 1
    },
    f = function(n, t) {
        return {
            x: n.x - t.x,
            y: n.y - t.y
        }
    },
    s = function(n, t) {
        return {
            x: n.x + t.x,
            y: n.y + t.y
        }
    },
    v = function(n, t) {
        return {
            x: n.x * t,
            y: n.y * t
        }
    },
    l = function(n) {
        return Math.sqrt(n.x * n.x + n.y * n.y)
    },
    d = function(n, t) {
        return l(f(n, t))
    },
    h = function(n) {
        return function(n, t) {
            return v(n, 1 / t)
        }(n, l(n) || 1)
    },
    p = function(n, t) {
        n.x = t.x, n.y = t.y
    },
    y = function(n, t, r) {
        return (1 - r) * n + r * t
    },
    M = function(n, t, r) {
        return {
            r: y(n.r, t.r, r),
            I: y(n.I, t.I, r),
            b: y(n.b, t.b, r),
            a: y(n.a, t.a, r)
        }
    },
    b = {
        x: .5,
        y: .5
    },
    m = {
        x: 1,
        y: 0
    },
    k = {
        x: 0,
        y: 1
    },
    x = {
        x: 1,
        y: 1
    },
    g = function(n) {
        return 564 * (Math.sin(100 * n.x + 6574 * n.y) + 1) % 1
    },
    w = function(n) {
        var t = function(n) {
                return {
                    x: c(n.x),
                    y: c(n.y)
                }
            }(n),
            r = function(n) {
                return {
                    x: ~~n.x,
                    y: ~~n.y
                }
            }(n),
            o = g(r),
            i = g(s(r, m)),
            u = y(o, i, t.x),
            a = g(s(r, k)),
            e = g(s(r, x)),
            f = y(a, e, t.x);
        return y(u, f, t.y)
    },
    A = function(n, t, r) {
        var o = i((r - n) / (t - n), 0, 1);
        return o * o * (3 - 2 * o)
    },
    B = function(n, t, r, o) {
        return void 0 === n && (n = 1), void 0 === t && (t = 1), void 0 === r && (r = 1), void 0 === o && (o = 1), {
            r: n,
            I: t,
            b: r,
            a: o
        }
    },
    z = function(n, t) {
        return {
            r: n.r * t,
            I: n.I * t,
            b: n.b * t,
            a: n.a
        }
    },
    D = function(n, t) {
        return {
            r: n.r + t.r * t.a,
            I: n.I + t.I * t.a,
            b: n.b + t.b * t.a,
            a: n.a + t.a
        }
    },
    E = function(n, t, o) {
        for (var u = r(n, t), a = u[0], e = u[1], c = e.getImageData(0, 0, n, t), f = new ArrayBuffer(c.data.length), s = new Uint8ClampedArray(f), v = new Uint32Array(f), l = {}, d = 0; d < t; d++)
            for (var h = 0; h < n; h++) {
                l.x = h / (n - 1), l.y = d / (t - 1);
                var p = o(l);
                v[d * n + h] = i(255 * p.a, 0, 255) << 24 | i(255 * p.b, 0, 255) << 16 | i(255 * p.I, 0, 255) << 8 | i(255 * p.r, 0, 255)
            }
        return c.data.set(s), e.putImageData(c, 0, 0), a
    },
    I = function(n, t) {
        var r = v(n, t),
            o = r.x,
            i = r.y;
        return o *= 1.1547, i += Math.floor(o) % 2 * .5, o = Math.abs(o % 1 - .5), i = Math.abs(i % 1 - .5), Math.abs(Math.max(1.5 * o + i, 2 * i) - 1)
    },
    G = function(n, t) {
        var r = A(.91, .94, t) - A(.41, .42, t);
        return n += r, .9 + .1 * Math.sin(6 * n) * .9 + .1 * Math.sin(4 * n) - .1 * w({
            x: 2 * (n + 4 + 5 * t),
            y: 80 * t
        }) + .2 * r
    },
    U = function(n) {
        var t = 4 / n,
            r = n / 4,
            o = B(.615, .705, 1, 1),
            i = B(1, 1, 1, 1);
        return E(Math.round(1.1 * n), Math.round(1.1 * n), function(n) {
            n = v(n, 1.1);
            var u = f(n, b),
                a = Math.atan2(u.y, u.x),
                e = 2 * l(u),
                c = .7 * A(.3, 1, 1 - I(n, r));
            c -= 1 * (1 - (A(.87, .8 - .1, e) - A(.6, .425, e)));
            var s = .4 * G(a, e),
                d = A(.8, .8 + t, e) + A(.5, .5 - t, e),
                h = M(z(o, c), z(i, s), d),
                p = .5 * A(1, .8, 2 * l(f(u, {
                    x: .04,
                    y: .04
                })) / 1.1),
                y = B(0, 0, 0, p);
            return M(h, y, A(1 - t, 1, e))
        })
    },
    S = function(n) {
        var t = 4 / n,
            r = n / 8,
            o = B(.815, .2705, .2, 1),
            i = B(1, 1, 1, 1);
        return E(Math.round(1.1 * n), Math.round(1.1 * n), function(n) {
            n = v(n, 1.1);
            var u = f(n, b),
                a = Math.atan2(u.y, u.x),
                e = 2 * l(u),
                c = .7 * A(.02, .41, 1 - I(n, r));
            c -= .6 * (1 - (A(.9025, .85 - .2, e) - A(.5, .255, e)));
            var s = .4 * G(a, e),
                d = A(.85, .85 + t, e) + A(.3, .3 - t, e),
                h = M(z(o, c), z(i, s), d),
                p = .5 * A(1, .8, 2 * l(f(u, {
                    x: .04,
                    y: .04
                })) / 1.1),
                y = B(0, 0, 0, p);
            return M(h, y, A(1 - t, 1, e))
        })
    },
    q = function(n) {
        return E(n, n, function(t) {
            var r = f(t, b),
                o = 2 * l(r),
                u = Math.atan2(r.y, r.x),
                a = u / (2 * Math.PI) + .5,
                e = (u / (2 * Math.PI) + .5 + .3 * o) * Math.round(8 + n / 50),
                s = a * Math.round(5 + n / 200),
                v = Math.min(c(e), c(1 - e)),
                d = A(0, .08, .5 * v - o + .7),
                h = 1 - A(.9, .2, o),
                p = 1.4 * o - .5 * d,
                M = function(n, t, r, o, u) {
                    var a = 2 * Math.min(c(n), c(1 - n)),
                        e = A(0, 8 * u, a - t),
                        f = A(o, o + u, 1 - t),
                        s = A(r + u, r, 1 - t);
                    return i(e + f - s, 0, 1)
                }(s, o, .45, .52, .02),
                m = .5 + .5 * G(1 * u, o);
            return p = y(y(h, p, d), .3 * M * m, M), B(p, p, p, d + (1 - h))
        })
    },
    C = function() {
        return E(21, 21, function(n) {
            var t = f(n, b),
                r = function(n) {
                    var t = 2 * l(n),
                        r = 2 * l(f(n, v(x, .05))),
                        o = .2 * A(1, .5, .8 * r),
                        i = A(1, .85, t);
                    return B(o, o, o, i)
                }(t),
                o = function(n) {
                    var t = 2 * l(n) * 1.2,
                        r = .25 * A(1, 0, t),
                        o = A(.99, .9, t);
                    return B(r, r, r, o)
                }(t),
                i = function(n) {
                    var t = 2 * l(n) * 1.5,
                        r = 1.01 * l(f(n, v(x, .14))),
                        o = A(1, .6, t) * A(.2, .5, r);
                    return B(o, o, o, o)
                }(t);
            return D(D(r, o), i)
        })
    },
    F = B(1, 1, 1, 1),
    L = function(n) {
        return E(80, 80, function(t) {
            var r = f(t, b),
                o = 1 - 2 * l(r),
                i = M(n, F, A(.6, .89, o)),
                u = A(0, 1, o);
            return B(i.r, i.I, i.b, u * u * u)
        })
    },
    O = function(n, t) {
        return E(t, t, function(t) {
            t = v(t, 1.1);
            var r = f(t, b),
                o = Math.atan2(r.y, r.x),
                i = 2 * l(r),
                u = A(1, .96, i),
                a = .3 * A(.9, .8, i) + .3;
            a -= A(.7, .6, i) * A(.2, .3, i) * .4;
            var e, c, s = (e = o + 3 * a, c = i, (.9 + .1 * Math.sin(6 * e) * .9 + .1 * Math.sin(4 * e) - .1 * w({
                    x: 2 * (e + 4 + 5 * c),
                    y: 80 * c
                })) * a),
                d = B(s, s, s, u),
                h = A(.35, .45, i) * A(.55, .45, i),
                p = M(d, n, h),
                y = .2 * A(1, .8, 2 * l(f(r, {
                    x: .04,
                    y: .04
                })) / 1.1),
                m = B(0, 0, 0, y);
            return M(p, m, A(.8, 1, i))
        })
    },
    N = function() {
        for (var n = r(1920, 1280), t = n[0], o = n[1], i = E(64, 64, function(n) {
                var t = v(n, 4),
                    r = 1 - .7 * A(.7, 1, I(t, 1));
                return B(.117 * r, .149 * r, .188 * r, 1)
            }), u = E(256, 144, function(n) {
                var t = .01,
                    r = A(0, .006, n.x) * A(1, .994, n.x) * A(0, t, n.y) * A(1, .99, n.y);
                return B(1, 1, 1, .04 * (1 - r))
            }), a = 0; a < 12; a++)
            for (var e = 0; e < 24; e++) o.drawImage(i, 54 * e, 63 * a);
        return o.drawImage(u, 0, 0, 1280, 720), t
    },
    P = function(n) {
        return document.getElementById(n)
    },
    T = P("title"),
    j = P("game"),
    H = P("loading"),
    J = P("menu"),
    K = P("levelDone"),
    Q = P("nextMsg"),
    R = P("nextBtn"),
    V = P("startBtn"),
    W = P("continueBtn"),
    X = P("content"),
    Y = P("reset"),
    Z = P("resetBtn"),
    $ = P("levelInfo"),
    _ = P("nodeInfo"),
    nn = P("description"),
    tn = P("skipBtn"),
    rn = P("backBtn"),
    on = function(n) {
        try {
            localStorage.setItem("level", "" + n)
        } catch (n) {}
    },
    un = function(n) {
        n.parentNode.removeChild(n)
    },
    an = function(n, t) {
        var r = Array.isArray(n) ? n : [n];
        r.forEach(function(n) {
            n.style.visibility = "visible", n.style.opacity = "0"
        }), kn(0, 1, .4, function(n) {
            r.forEach(function(t) {
                t.style.opacity = n.toString()
            })
        }, function() {
            t && t()
        })
    },
    en = function(n, t) {
        var r = Array.isArray(n) ? n : [n];
        kn(1, 0, .4, function(n) {
            r.forEach(function(t) {
                t.style.opacity = n.toString()
            })
        }, function() {
            r.forEach(function(n) {
                n.style.visibility = "hidden"
            }), t && t()
        })
    },
    cn = function(n) {
        var t = !1,
            r = {
                x: 0,
                y: 0
            },
            o = [],
            i = [],
            u = [],
            a = function(t) {
                var o = n.getBoundingClientRect();
                r.x = t.clientX - o.left, r.y = t.clientY - o.top, t.preventDefault()
            },
            e = function(n) {
                t = !0, o.forEach(function(n) {
                    var t = n[1].G;
                    t && t(), u.push(n)
                }), n.preventDefault()
            },
            c = function(n) {
                t = !1, u.forEach(function(n) {
                    var t = n[1].U;
                    t && t()
                }), u.length = 0
            };
        document.addEventListener("mousemove", a), document.addEventListener("mousedown", e), document.addEventListener("mouseup", c);
        return {
            update: function() {
                for (var n = i.length - 1; n >= 0; --n) {
                    var u = (a = i[n])[1];
                    d(r, a[0].s) <= a[0].g.size && (u.S && u.S(), i.splice(n, 1), o.push(a))
                }
                for (n = o.length - 1; n >= 0; --n) {
                    var a;
                    u = (a = o[n])[1], t && u.q && u.q(), d(r, a[0].s) > a[0].g.size && (u.C && u.C(), o.splice(n, 1), i.push(a))
                }
            },
            F: function(n, t) {
                i.push([n, t])
            },
            L: r,
            O: function() {
                return t
            },
            o: function() {
                document.removeEventListener("mousemove", a), document.removeEventListener("mousedown", e), document.removeEventListener("mouseup", c)
            },
            N: o
        }
    },
    fn = {
        P: [{
            u: [
                [460, 207, 70],
                [468, 516, 70]
            ],
            m: [],
            p: [],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [440, 540, 60],
                [846, 556, 60],
                [645, 173, 90]
            ],
            m: [],
            p: [
                [777, 369, 110],
                [249, 461, 70]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [871, 447, 50],
                [659, 590, 50],
                [629, 267, 40]
            ],
            m: [
                [438, 561, 40],
                [497, 148, 40]
            ],
            p: [
                [241, 435, 70],
                [675, 422, 90],
                [324, 215, 50]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [872, 496, 130],
                [508, 234, 60],
                [508, 486, 60],
                [871, 190, 130]
            ],
            m: [
                [234, 525, 40],
                [237, 182, 40]
            ],
            p: [
                [667, 288, 60],
                [669, 427, 60],
                [593, 132, 60],
                [597, 588, 60]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [845, 156, 70],
                [595, 443, 60],
                [668, 609, 60],
                [396, 416, 50]
            ],
            m: [
                [832, 396, 40],
                [556, 247, 40]
            ],
            p: [
                [696, 204, 60],
                [721, 392, 60],
                [498, 345, 50]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [664, 338, 70],
                [365, 171, 90],
                [929, 170, 90],
                [1011, 559, 80],
                [372, 558, 90]
            ],
            m: [
                [729, 561, 40],
                [1149, 266, 40]
            ],
            p: [
                [757, 203, 70],
                [846, 375, 70],
                [585, 549, 80],
                [1150, 429, 50]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [502, 259, 60],
                [508, 458, 60],
                [979, 356, 50],
                [346, 573, 60],
                [319, 141, 60]
            ],
            m: [
                [724, 361, 40],
                [720, 142, 40]
            ],
            p: [
                [609, 353, 60],
                [379, 451, 50],
                [848, 360, 70]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [957, 156, 70],
                [378, 570, 70],
                [507, 109, 60]
            ],
            m: [
                [568, 536, 40],
                [382, 198, 40],
                [659, 112, 40],
                [940, 348, 40]
            ],
            p: [
                [756, 445, 100],
                [1122, 234, 50]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [629, 130, 40],
                [811, 482, 50],
                [385, 491, 50],
                [386, 317, 50],
                [976, 569, 40],
                [844, 139, 60],
                [1161, 138, 50]
            ],
            m: [
                [222, 230, 40],
                [216, 587, 30]
            ],
            p: [
                [619, 367, 160],
                [1015, 255, 130]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [922, 509, 150],
                [257, 552, 60],
                [201, 200, 50],
                [509, 519, 50],
                [520, 134, 50],
                [937, 257, 50],
                [1111, 133, 50]
            ],
            m: [
                [678, 465, 40],
                [679, 291, 40]
            ],
            p: [
                [887, 113, 80],
                [392, 438, 70],
                [699, 573, 50],
                [1163, 468, 50]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [228, 193, 150],
                [326, 563, 80],
                [557, 209, 70],
                [785, 199, 50],
                [1043, 593, 80],
                [1015, 188, 130],
                [791, 548, 50],
                [543, 544, 50],
                [511, 373, 30],
                [685, 333, 30]
            ],
            m: [
                [687, 446, 30],
                [1205, 455, 30]
            ],
            p: [
                [442, 116, 50],
                [982, 400, 50],
                [1203, 265, 50],
                [1185, 563, 50],
                [776, 382, 60],
                [408, 428, 50]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [669, 355, 80],
                [668, 187, 50],
                [666, 70, 30],
                [668, 514, 50],
                [673, 653, 30],
                [473, 361, 50],
                [852, 353, 50],
                [986, 348, 30],
                [335, 361, 30]
            ],
            m: [],
            p: [
                [804, 476, 50],
                [552, 244, 60],
                [857, 174, 90],
                [489, 541, 80]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [549, 114, 60],
                [213, 345, 30],
                [389, 186, 50],
                [834, 93, 70],
                [297, 272, 40],
                [389, 564, 50],
                [606, 542, 50],
                [815, 566, 50]
            ],
            m: [],
            p: [
                [839, 300, 130],
                [1062, 343, 80],
                [483, 354, 50],
                [337, 419, 70],
                [485, 537, 30],
                [204, 507, 50]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [402, 380, 90],
                [758, 379, 90],
                [890, 195, 50],
                [324, 166, 50],
                [1036, 91, 40],
                [1038, 461, 50],
                [1055, 622, 40]
            ],
            m: [
                [600, 100, 40],
                [595, 617, 40]
            ],
            p: [
                [159, 251, 50],
                [733, 156, 70],
                [886, 553, 80],
                [988, 303, 80],
                [1167, 238, 50],
                [1082, 536, 30]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [647, 360, 160],
                [326, 233, 30],
                [462, 111, 30],
                [646, 71, 30],
                [819, 120, 30],
                [932, 277, 30],
                [930, 468, 30],
                [809, 602, 30],
                [626, 644, 30],
                [438, 579, 30],
                [334, 404, 30]
            ],
            m: [
                [188, 119, 30],
                [192, 568, 30]
            ],
            p: [
                [1069, 367, 90],
                [354, 134, 50],
                [561, 106, 40],
                [828, 232, 50],
                [855, 392, 50],
                [711, 577, 50],
                [447, 466, 50],
                [431, 258, 60]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }, {
            u: [
                [335, 304, 50],
                [655, 299, 60],
                [961, 191, 50],
                [318, 584, 50],
                [650, 580, 50],
                [1007, 591, 50],
                [346, 115, 40],
                [1139, 136, 50],
                [1198, 581, 30],
                [901, 497, 30]
            ],
            m: [],
            p: [
                [1090, 294, 70],
                [985, 487, 40],
                [765, 482, 60],
                [846, 192, 50],
                [538, 149, 50],
                [1037, 134, 30],
                [1135, 530, 30]
            ],
            start: [50, 360],
            finish: [1230, 360],
            end: [110, 360]
        }]
    },
    sn = function(n) {
        var r, o, u = {
                x: 0,
                y: 0
            },
            a = [],
            e = !1,
            c = !1;
        return {
            h: function(i) {
                !i.v || i.v.type !== t.v && i.v.type !== t.k || a.push(i), i.finish && (o = i), i.g && n.F(i, {
                    S: function() {
                        c = !0, n.O() || (document.body.style.cursor = "pointer", r = i, i.l.T = !0)
                    },
                    C: function() {
                        document.body.style.cursor = "default", c = !1, e || (i.l.T = !1)
                    },
                    G: function() {
                        e = !0, p(u, f(n.L, i.s))
                    },
                    U: function() {
                        e = !1, c || (i.l.T = !1)
                    },
                    q: function() {}
                })
            },
            update: function(t) {
                if (n.update(), r) {
                    e && p(r.s, f(n.L, u));
                    var c = r.s;
                    c.x = i(c.x, 0, 1280), c.y = i(c.y, 0, 720), a.forEach(function(n) {
                        if (n !== r) {
                            var t = n.s,
                                o = 10 + n.v.size;
                            if (d(c, t) < o) {
                                var i = h(f(c, t));
                                0 == i.x && 0 == i.y && (i.x = 1);
                                var u = v(i, o);
                                r.s = s(t, u)
                            }
                        }
                    }), d(c, o.s) < 30 ? (o.finish.connected = !0, p(r.s, o.s)) : o.finish.connected = !1
                }
            }
        }
    },
    vn = function(n) {
        var r = [],
            o = n.j,
            i = n.p,
            u = n.m,
            a = n.H,
            e = n.finish,
            c = n.start;
        return {
            h: function(n) {
                n.l && r.push(n)
            },
            l: function(f, s) {
                r.forEach(function(r) {
                    switch (r.l.type) {
                        case t.v:
                            f.drawImage(o[r.v.size], r.s.x - r.v.size - 6, r.s.y - r.v.size - 6), f.drawImage(n.J, r.s.x - 11, r.s.y - 11), r.v.K ? f.drawImage(n.R, r.s.x - 40, r.s.y - 40) : r.v.V && f.drawImage(n.W, r.s.x - 40, r.s.y - 40);
                            break;
                        case t.k:
                            f.drawImage(u[r.v.size], r.s.x - r.v.size - 6, r.s.y - r.v.size - 6);
                            break;
                        case t.M:
                            f.save(), f.translate(r.s.x, r.s.y), f.rotate(s);
                            var v = i[r.M.size];
                            f.drawImage(v, -v.width / 2, -v.height / 2), f.restore();
                            break;
                        case t.finish:
                            f.drawImage(e, r.s.x - 32, r.s.y - 32);
                            break;
                        case t.start:
                            f.drawImage(c, r.s.x - 24, r.s.y - 24);
                            break;
                        case t.end:
                            f.drawImage(a, r.s.x - 32, r.s.y - 32), r.l.T ? (f.globalAlpha = .8 + .2 * Math.sin(6 * s), f.drawImage(n.X, r.s.x - 31, r.s.y - 31)) : (f.globalAlpha = .2 + .2 * Math.sin(3 * s), f.drawImage(n.X, r.s.x - 31, r.s.y - 31)), f.globalAlpha = 1
                    }
                })
            }
        }
    },
    ln = function() {
        var n = [];
        return {
            h: function(t) {
                t.A && n.push(t)
            },
            l: function(t) {
                n.forEach(function(n) {
                    for (var r = n.A.attachments, o = 0; o < r.length - 1; o++) {
                        var i = r[o],
                            u = r[o + 1];
                        t.save(), i.Y && t.setLineDash([5, 10]), i.Z ? (t.strokeStyle = "#d04533", t.lineWidth = 5) : (t.strokeStyle = "white", t.lineWidth = 3), t.lineCap = "round", t.beginPath(), t.moveTo(i.$.x, i.$.y), t.lineTo(u._.x, u._.y), t.stroke(), t.restore()
                    }
                })
            }
        }
    },
    dn = function(n, t) {
        var o = [],
            i = {},
            u = {},
            a = {};
        [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160].forEach(function(n) {
            o.push(function() {
                i[n] = U(2 * n + 10)
            })
        }), [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160].forEach(function(n) {
            o.push(function() {
                u[n] = q(2 * n + 6)
            })
        }), [30, 40, 50, 60, 70, 80].forEach(function(n) {
            o.push(function() {
                a[n] = S(2 * n + 10)
            })
        });
        var e, c = C(),
            s = L(B(0, 1, 0)),
            v = L(B(1, 0, 0)),
            d = O(B(.2, .6, .2), 70),
            h = O(B(.2, .2, .2), 52),
            p = (e = B(0, 1, 0), E(62, 62, function(n) {
                var t = f(n, b),
                    r = 1 - 2 * l(t),
                    o = M(e, F, A(.45, .5, r) * A(.55, .5, r)),
                    i = A(0, .5, r) * A(1, .5, r);
                return B(o.r, o.I, o.b, i * i * i)
            })),
            y = O(B(1, .4, .4), 70),
            m = r(450, 264),
            k = m[0],
            x = m[1];
        k.className = "tutorial", x.font = "20px sans-serif", x.fillStyle = "#ccc", x.fillText("1. Drag the cable ...", 20, 50), x.drawImage(d, 358, 10), x.fillText("2. ...around the power nodes...", 20, 140), x.drawImage(U(80), 350, 90), x.fillText("3. ...and plug it into the socket!", 20, 230), x.drawImage(y, 358, 190);
        var g = r(450, 100),
            w = g[0],
            z = g[1];
        w.className = "tutorial", z.font = "20px sans-serif", z.fillStyle = "#ccc", z.fillText("Isolated cables can overlap others ", 20, 55), z.drawImage(S(80), 358, 10);
        var D = o.length,
            I = 0;
        ! function r() {
            var e = o.shift();
            e ? (e(), n(100 / D * ++I), requestAnimationFrame(r)) : t({
                j: i,
                p: u,
                m: a,
                W: s,
                R: v,
                J: c,
                H: d,
                X: p,
                finish: y,
                nn: k,
                tn: w,
                start: h
            })
        }()
    },
    hn = function() {
        var n = [],
            t = [];
        return {
            i: function(t) {
                n.push(t)
            },
            h: function(r) {
                t.push(r), n.forEach(function(n) {
                    n.h(r)
                })
            },
            o: function() {
                n.forEach(function(n) {
                    return n.o && n.o()
                })
            },
            entities: t
        }
    },
    pn = function(t) {
        for (var r = 0; r < t.length - 1; r++) {
            var o = t[r],
                i = t[r + 1],
                u = e(o.B.s, o.B.v.size, i.B.s, i.B.v.size),
                a = o.D == n.left ? i.D == n.left ? 1 : 3 : i.D == n.left ? 2 : 0;
            u[a], o.$ = u[a][0], i._ = u[a][1]
        }
    },
    yn = function(n, t, r, o, i) {
        return r.filter(function(r) {
            return r != o && r != i && u(n, t, r.s, r.v.size)
        }).sort(function(t, r) {
            return a(t.s, n) > a(r.s, n) ? 1 : -1
        })
    },
    Mn = function(r) {
        var o, i = [],
            a = [],
            e = [],
            c = 0,
            s = 0;
        return {
            h: function(n) {
                n.v && (i.push(n), n.v.type == t.v && (s++, _.innerHTML = "0 / " + s)), n.A && e.push(n), n.M && a.push(n), n.finish && (o = n)
            },
            update: function(v) {
                e.forEach(function(e) {
                    var v = e.A.attachments;
                    e.A.K = !1, v.forEach(function(n) {
                        n.Y = !1
                    }), i.forEach(function(n) {
                        n.v.V = n.v.K = !1
                    });
                    var l = 0;
                    pn(v),
                        function(t, r) {
                            var o, i, u, a;
                            do {
                                o = !0;
                                for (var e = 0; e < t.length - 1; e++) {
                                    var c = t[e],
                                        f = t[e + 1],
                                        s = yn(c.$, f._, r, c.B, f.B)[0];
                                    if (s) {
                                        if (!s.v.rn) {
                                            s.v.rn = !0;
                                            var v = {
                                                B: s,
                                                D: (i = c.$, u = f._, a = s.s, (u.x - i.x) * (a.y - i.y) - (u.y - i.y) * (a.x - i.x) > 0 ? n.left : n.right)
                                            };
                                            t.splice(e + 1, 0, v), o = !1, pn([c, v, f]);
                                            break
                                        }
                                        c.Y = !0
                                    }
                                }
                            } while (!o)
                        }(v, i),
                        function(t) {
                            var r;
                            do {
                                r = !0;
                                for (var o = 1; o < t.length - 1; o++) {
                                    var i = t[o - 1],
                                        u = t[o],
                                        a = t[o + 1],
                                        e = f(i.$, u._),
                                        c = f(u.$, a._),
                                        s = Math.atan2(c.y, c.x) - Math.atan2(e.y, e.x);
                                    if (s < 0 && (s += 2 * Math.PI), u.D == n.left && s > 1.8 * Math.PI || u.D == n.right && s < .2 * Math.PI) {
                                        t.splice(o, 1), u.B.v.rn = !1, r = !1, pn([i, a]);
                                        break
                                    }
                                }
                            } while (!r)
                        }(v);
                    var d, h, p, y, M, b, m, k, x, g, w = !1;
                    e.A.attachments.forEach(function(n) {
                        n.B.v.type == t.k && (w = !w), n.Z = w
                    });
                    for (var A = 0; A < v.length - 1; A++) {
                        var B = v[A],
                            z = v[A + 1];
                        if (!B.Z)
                            for (var D = 0; D < v.length - 1; D++) {
                                var E = v[D],
                                    I = v[D + 1];
                                E.Z || (d = B.$, h = z._, p = E.$, y = I._, void 0, void 0, void 0, void 0, void 0, void 0, M = h.x - d.x, b = h.y - d.y, m = y.x - p.x, k = y.y - p.y, x = (-b * (d.x - p.x) + M * (d.y - p.y)) / (-m * b + M * k), g = (m * (d.y - p.y) - k * (d.x - p.x)) / (-m * b + M * k), x >= 0 && x <= 1 && g >= 0 && g <= 1 && (B.Y = E.Y = !0))
                            }
                    }
                    for (A = 0; A < v.length - 1; A++)
                        for (B = v[A], z = v[A + 1], D = 0; D < a.length; D++) u(B.$, z._, a[D].s, a[D].M.size) && (B.Y = !0, e.A.K = !0);
                    var G = !0;
                    e.A.attachments.every(function(n) {
                        return !!G && (!(!n.Z || n.Y) || (n.B.v.V ? (n.B.v.K = !0, e.A.K = !0, !1) : (n.B.v.V = !0, n.Y ? G = !1 : n.B.v.type == t.v && l++, !0)))
                    }), G && o.finish.connected && !e.A.K && l === s && r(), l != c && (_.innerHTML = l + " / " + s), c = l
                })
            }
        }
    };
! function(n) {
    n[n.left = -1] = "left", n[n.right = 1] = "right"
}(n || (n = {})),
function(n) {
    n[n.v = 0] = "spool", n[n.start = 1] = "start", n[n.end = 2] = "end", n[n.M = 3] = "block", n[n.finish = 4] = "finish", n[n.k = 5] = "isolator"
}(t || (t = {}));
var bn = requestAnimationFrame,
    mn = function(n) {
        var t = !1,
            r = function(o) {
                n(.001 * o), t || bn(r), o
            };
        return bn(r),
            function() {
                t = !0
            }
    },
    kn = function(n, t, r, o, i) {
        var u = performance.now(),
            a = function(e) {
                var c = 1 / r * (e - u) * .001;
                c < 1 ? (o(n + (t - n) * c), bn(a)) : (o(t), bn(i))
            };
        a(u)
    },
    xn = function(n, t, r) {
        var i = o(),
            u = r,
            a = function() {
                var r;
                0 == u && (r = t.nn, j.appendChild(r), an(r)), 2 == u && (r = t.tn, j.appendChild(r), an(r));
                var o = i.t(fn.P[u], t, function() {
                    r && en(r, function() {
                        un(r)
                    }), u < fn.P.length - 1 ? (on(++u), en(Y), an([K], function() {
                        R.onclick = function() {
                            R.onclick = null, en([K, o.canvas, $, _], function() {
                                un(o.canvas), a()
                            })
                        }
                    })) : (Q.innerHTML = "Thanks for playing!", R.innerHTML = "AGAIN", an(K, function() {
                        R.addEventListener("click", function(n) {
                            location.reload()
                        })
                    }), on(0))
                });
                n.appendChild(o.canvas), $.innerHTML = "Level " + (u + 1), an([o.canvas, Y, $, _]);
                var e = function() {
                    r && en(r, function() {
                        un(r)
                    }), rn.onclick = tn.onclick = Z.onclick = null, en([o.canvas, Y, $, _], function() {
                        o.o(), un(o.canvas), a()
                    })
                };
                Z.onclick = e, tn.onclick = function() {
                    u > fn.P.length - 2 || (u++, e())
                }, rn.onclick = function() {
                    u < 1 || (u--, e())
                }
            };
        a()
    };
an(T, function() {
    var n = r(200, 7),
        t = n[0],
        o = n[1];
    t.id = "loadingbar", H.appendChild(t), an(t), o.strokeStyle = "grey", o.fillStyle = "grey", o.lineWidth = 1, o.strokeRect(.5, .5, 199, 4), dn(function(n) {
        o.fillRect(.5, .5, 1.99 * n, 4)
    }, function(n) {
        en(t, function() {
            an([J, nn]);
            var t = function() {
                try {
                    return parseInt(localStorage.getItem("level")) || 0
                } catch (n) {
                    return 0
                }
            }();
            W.style.visibility = t ? "visible" : "hidden";
            var r = function(t) {
                V.onclick = W.onclick = null, en([T, J, nn], function() {
                    xn(X, n, t)
                })
            };
            V.onclick = function() {
                on(0), r(0)
            }, W.onclick = function() {
                r(t)
            }
        })
    })
});