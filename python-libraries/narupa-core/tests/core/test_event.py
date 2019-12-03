from narupa.core import Event


def test_invoke_nocallbacks():
    event = Event()
    event.publish('argument')


def test_invoke_callback():
    event = Event()

    def callback():
        callback.called = True

    callback.called = False

    event.add_callback(callback)

    assert callback.called == False

    event.publish()

    assert callback.called == True


def test_invoke_callback_then_remove():
    event = Event()

    def callback():
        callback.called += 1

    callback.called = 0

    event.add_callback(callback)

    assert callback.called == 0

    event.publish()

    assert callback.called == 1

    event.remove_callback(callback)

    event.publish()

    assert callback.called == 1
