# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import github.GithubObject

import github.HookResponse


class Hook(github.GithubObject.GithubObject):
    @property
    def active(self):
        self._completeIfNotSet(self._active)
        return self._NoneIfNotSet(self._active)

    @property
    def config(self):
        self._completeIfNotSet(self._config)
        return self._NoneIfNotSet(self._config)

    @property
    def created_at(self):
        self._completeIfNotSet(self._created_at)
        return self._NoneIfNotSet(self._created_at)

    @property
    def events(self):
        self._completeIfNotSet(self._events)
        return self._NoneIfNotSet(self._events)

    @property
    def id(self):
        self._completeIfNotSet(self._id)
        return self._NoneIfNotSet(self._id)

    @property
    def last_response(self):
        self._completeIfNotSet(self._last_response)
        return self._NoneIfNotSet(self._last_response)

    @property
    def name(self):
        self._completeIfNotSet(self._name)
        return self._NoneIfNotSet(self._name)

    @property
    def updated_at(self):
        self._completeIfNotSet(self._updated_at)
        return self._NoneIfNotSet(self._updated_at)

    @property
    def url(self):
        self._completeIfNotSet(self._url)
        return self._NoneIfNotSet(self._url)

    def delete(self):
        headers, data = self._requester.requestJsonAndCheck(
            "DELETE",
            self.url,
            None,
            None
        )

    def edit(self, name, config, events=github.GithubObject.NotSet, add_events=github.GithubObject.NotSet, remove_events=github.GithubObject.NotSet, active=github.GithubObject.NotSet):
        assert isinstance(name, (str, unicode)), name
        assert isinstance(config, dict), config
        assert events is github.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in events), events
        assert add_events is github.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in add_events), add_events
        assert remove_events is github.GithubObject.NotSet or all(isinstance(element, (str, unicode)) for element in remove_events), remove_events
        assert active is github.GithubObject.NotSet or isinstance(active, bool), active
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not github.GithubObject.NotSet:
            post_parameters["events"] = events
        if add_events is not github.GithubObject.NotSet:
            post_parameters["add_events"] = add_events
        if remove_events is not github.GithubObject.NotSet:
            post_parameters["remove_events"] = remove_events
        if active is not github.GithubObject.NotSet:
            post_parameters["active"] = active
        headers, data = self._requester.requestJsonAndCheck(
            "PATCH",
            self.url,
            None,
            post_parameters
        )
        self._useAttributes(data)

    def test(self):
        headers, data = self._requester.requestJsonAndCheck(
            "POST",
            self.url + "/test",
            None,
            None
        )

    def _initAttributes(self):
        self._active = github.GithubObject.NotSet
        self._config = github.GithubObject.NotSet
        self._created_at = github.GithubObject.NotSet
        self._events = github.GithubObject.NotSet
        self._id = github.GithubObject.NotSet
        self._last_response = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet
        self._updated_at = github.GithubObject.NotSet
        self._url = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "active" in attributes:  # pragma no branch
            assert attributes["active"] is None or isinstance(attributes["active"], bool), attributes["active"]
            self._active = attributes["active"]
        if "config" in attributes:  # pragma no branch
            assert attributes["config"] is None or isinstance(attributes["config"], dict), attributes["config"]
            self._config = attributes["config"]
        if "created_at" in attributes:  # pragma no branch
            assert attributes["created_at"] is None or isinstance(attributes["created_at"], (str, unicode)), attributes["created_at"]
            self._created_at = self._parseDatetime(attributes["created_at"])
        if "events" in attributes:  # pragma no branch
            assert attributes["events"] is None or all(isinstance(element, (str, unicode)) for element in attributes["events"]), attributes["events"]
            self._events = attributes["events"]
        if "id" in attributes:  # pragma no branch
            assert attributes["id"] is None or isinstance(attributes["id"], (int, long)), attributes["id"]
            self._id = attributes["id"]
        if "last_response" in attributes:  # pragma no branch
            assert attributes["last_response"] is None or isinstance(attributes["last_response"], dict), attributes["last_response"]
            self._last_response = None if attributes["last_response"] is None else github.HookResponse.HookResponse(self._requester, attributes["last_response"], completed=False)
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
        if "updated_at" in attributes:  # pragma no branch
            assert attributes["updated_at"] is None or isinstance(attributes["updated_at"], (str, unicode)), attributes["updated_at"]
            self._updated_at = self._parseDatetime(attributes["updated_at"])
        if "url" in attributes:  # pragma no branch
            assert attributes["url"] is None or isinstance(attributes["url"], (str, unicode)), attributes["url"]
            self._url = attributes["url"]
